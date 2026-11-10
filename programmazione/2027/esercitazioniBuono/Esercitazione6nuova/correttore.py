#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (C) 2019, 2020, 2021, 2022, 2023, 2024 by Massimo Lauria <massimo.lauria@uniroma1.it>
"""Correttore per gli esami di Informatica (almeno la parte di programmazione)

Questa utility serve a correggere gli esercizi di programmazione
e calcolare il voto della prova.
"""

import os
import sys
import csv
import subprocess
import argparse
import tempfile
from contextlib import contextmanager
from contextlib import redirect_stdout
from datetime import date
from io import StringIO
import shutil

# Configurazione
file_studente = 'studente.txt'
file_esame = 'esame.txt'
file_template = ['nome:', 'cognome:', 'matricola:']
id_aule = {'c15': 'XV', 'c16': 'XVI', 'c17': 'XVII'}
default_timeout = 2  # 2 secondi dovrebbero essere sufficienti
py_cmd = 'python3'
tex_cmd = 'pdflatex'

# Test data, to be loaded from file
esame_data = None
esame_path = None
esame_attachments = []


def execute_test_program(solutionfpath, testfpath):
    """Esegue il programma ed estrae l'esito

    Il programma dovrebbe essere uno unit test. Nel caso il test
    esegua correttamente il risultato dovrebbe essere un dizionario
    {'status': status, 'errors': num_errors , 'failures': num_failures}

    status può essere: executed, broken, missing
    - executed, lo unit test è stato eseguito
    - broken, il test non ha funzionato
    - timeout, il test è andato in timeout
    - missing, il file di soluzione non è presente

    L'esecuzione del test avviene nella cartella corrente.

    ASSUNZIONI:
       il test restituisce -1 se qualcosa è andato male
       il test restituisce 1 se ci sono test falliti o errati
       il test restituisce 0 se non ci sono errori

    Parameters:
    -----------
    solutionfpath:
        il nome del programma soluzione
    testfpath:
        il nome del programma

    Return:
    -------
    dizionario con i risultati
    """
    result = {}
    if not os.path.isfile(testfpath):
        result['status'] = 'no test'
        return result

    if not os.path.isfile(solutionfpath):
        result['status'] = 'missing'
        return result

    if not os.path.isfile(solutionfpath):
        result['status'] = 'broken'
        return result

    # Run the test
    try:
        outcome = subprocess.run([py_cmd, testfpath],
                                 encoding='utf-8',
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 timeout=default_timeout)
    except subprocess.TimeoutExpired:
        result['status'] = 'timeout'
        return result

    # test did not execute at all
    if outcome.returncode == 255:
        result['status'] = 'broken'
        return result
    # no errors or failues
    elif outcome.returncode in [0, 1]:
        pass
    else:
        raise RuntimeError("Il test ha restituito un codice non previsto")

    # maybe some errors of failures, we need to parse the output
    errorlines = outcome.stderr.splitlines()
    resultline = None
    totalnumber = None
    # Looking for outcome
    for i in range(1, len(errorlines) + 1):
        if errorlines[-i].find("FAILED") == 0 or errorlines[-i] == 'OK':
            resultline = errorlines[-i]
            break
    for i in range(1, len(errorlines) + 1):
        if errorlines[-i].find("Ran") == 0:
            totalnumber = int(errorlines[-i].split()[1])
            break

    if resultline is None:
        raise RuntimeError(
            "Il test è stato eseguito ma non è possibile estrarre il risultato"
        )
    if not isinstance(totalnumber, int):
        raise RuntimeError(
            "Il test è stato eseguito ma non è possibile estrarre il numero dei casi"
        )
    result['status'] = 'executed'
    result['errors'] = 0
    result['failures'] = 0
    result['total'] = totalnumber
    result['stderr'] = outcome.stderr

    if resultline == 'OK':
        return result

    # Otherwise resultline has the form "FAILED (failures=4, errors=10)"
    resultline = resultline[len('FAILED'):].strip()
    tmp = []
    for c in resultline:
        if c in '()=,':
            tmp.append(' ')
        else:
            tmp.append(c)
    resultline = ''.join(tmp).split()
    try:
        pos = resultline.index('failures')
        result['failures'] = int(resultline[pos + 1])
    except ValueError:
        pass
    try:
        pos = resultline.index('errors')
        result['errors'] = int(resultline[pos + 1])
    except ValueError:
        pass

    return result


def execute_test_for_student():
    """Esegue tutti i test per gli esercizi

    Crea una cartella temporanea dove vengono caricati i file con le
    soluzioni (della cartella corrente) e i file di test dalla
    cartella designata dalle informazioni che riguardano l'esercizio.

    Questa funzione deve essere eseguita quando la cartella corrente
    è la cartella di uno studente.

    Return:
    -------
    una lista di triple contenenti: l'indice di un esercizio i,
    e l'esito dei test pubblici e segreti dell'esercizio i-esimo
    """

    tempdir = tempfile.mkdtemp()

    # Copy all test files in a temporary directory
    for eid, score, eauto in esame_data:

        sol = f"{eid}.py"
        pub = f"test_{eid}.py"
        sec = f"test_{eid}_secret.py"

        # Copy the solution file from current directory
        solsrc = os.path.join(os.path.curdir, sol)
        soldst = os.path.join(tempdir, sol)
        try:
            shutil.copyfile(solsrc, soldst)
        except FileNotFoundError:
            pass

        # Copy the test files from test directory
        pubsrc = os.path.join(esame_path, pub)
        pubdst = os.path.join(tempdir, pub)
        secsrc = os.path.join(esame_path, sec)
        secdst = os.path.join(tempdir, sec)
        try:
            shutil.copyfile(pubsrc, pubdst)
        except FileNotFoundError:
            pass

        try:
            shutil.copyfile(secsrc, secdst)
        except FileNotFoundError:
            pass

    results = []

    # Copy all exam attachments
    for fname in esame_attachments:
        asrc = os.path.join(esame_path, fname)
        adst = os.path.join(tempdir, fname)
        try:
            shutil.copyfile(asrc, adst)
        except FileNotFoundError:
            pass

    for i in range(len(esame_data)):
        eid, score, eauto = esame_data[i]

        sol = f"{eid}.py"
        pub = f"test_{eid}.py"
        sec = f"test_{eid}_secret.py"

        with working_dir(tempdir):
            pubres = execute_test_program(sol, pub)
            secres = execute_test_program(sol, sec)
            results.append((i,pubres, secres))

    shutil.rmtree(tempdir, ignore_errors=True)
    return results


def setup_command_line_parsers(progname):
    """Inizializza le opzioni a linea di comando

    Parameters:
    -----------
    progname:
        il nome del programma

    Return:
    -------
    l'oggetto parser per la linea di comando
    """

    parser = argparse.ArgumentParser(
        prog=progname, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--format',
                        '-f',
                        choices=['tex', 'csv', 'pdf', 'org','xlsx'],
                        default=['csv'],
                        nargs='+',
                        help="""
Formato in cui produrre l'esito dei compiti.
   * 'csv'  formato compatibile con i fogli elettronici.
   * 'pdf'  genera un documento pdf via latex,
   * 'tex'  genera il sorgente latex senza compilarlo,
   * 'org'  tabella in formato org-mode
   * 'xlsx' foglio excel (richiede pacchetto python xlsxwriter)

Si possono generate più formati simultaneamene (e.g. 'pdf cvs')
(default: csv\n""")

    parser.add_argument('examdir',
                        metavar='<cartella esame>',
                        default=os.path.curdir,
                        action='store',
                        nargs='?',
                        help="La cartella con le specifiche dell'esame\n"
                        "(default: cartella corrente)\n")

    parser.add_argument('solutiondir',
                        metavar='<cartella soluzioni>',
                        default=os.path.curdir,
                        action='store',
                        nargs='?',
                        help="La cartella con le soluzioni da valutare\n"
                        "(default: cartella corrente)\n")

    parser.add_argument('--output',
                        '-o',
                        default='out',
                        help="Salva i risultati nei file OUTPUT.ext,\n"
                        "dove 'ext' corrisponde al formato selezionato.\n"
                        "(default: 'out')\n")

    parser.add_argument(
        '--scan',
        '-s',
        default=False,
        action='store_true',
        help="Non correggere. "
        "Esegui solo la scansione degli studenti. (default: False)")

    parser.add_argument(
        '--rankby',
        '-r',
        default='cognome',
        action='store',
        help="Campo rispetto al quale ordinare. "
        "Ordina rispetto al campo scelto. (default: 'cognome')")

    parser.add_argument(
        '--errors',
        '-e',
        default=False,
        action='store_true',
        help="Show test error, only in single student mode. (defaut: false)")

    g = parser.add_mutually_exclusive_group()
    g.add_argument(
        '--anonymize',
        '-a',
        action='store_true',
        default=False,
        help="Maschera le cifre della matricola. "
        "Ne maschera il più possibile mantenendo unicità (default: False)"
    )

    g.add_argument(
        '--cover',
        '-c',
        metavar="C",
        type=int,
        action='store',
        default=0,
        help="Nascondi N cifre della matricola. (default: 0)"
    )

    return parser


@contextmanager
def working_dir(path):
    oldwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(oldwd)


def allegati_compito(spec_compito):
    "Estrae i file allegati indicati nelle specifiche"
    basename = os.path.basename(spec_compito)

    cue="allegati:"
    with open(spec_compito) as spec:
        lines=spec.readlines()
    attachments=[]
    for line in lines:
        if line[:len(cue)].lower() == cue:
            attachments.extend(line[len(cue):].strip().split())

    return attachments

def estrazione_specifiche_compito(spec_compito):
    """
    Linee permesse nel compito

    esercizio  <punteggio>
    esercizio  <punteggio> auto
    esercizio  <punteggio> manuale
    esercizio

    Le prime due righe indicano un esercizio con punteggio e correzione automatica
    La terza un esercizio con punteggio e correzione manuale
    La quarta un esercizio senza punteggio

    Se il file contiene una riga che inizia con 'allegati:' questa
    indica i file allegati al compito. """
    basename = os.path.basename(spec_compito)

    cue="descrizione:"
    att_cue="allegati:"
    with open(spec_compito) as spec:
        lines=spec.readlines()
    desc = None
    speclines=[]
    attachments=[]
    for i,line in enumerate(lines,start=1):

        if len(line.strip())==0: continue

        if line[:len(cue)].lower() == cue:
            if desc is not None:
                print("Error: il file del compito ha più di una descrizione...",file=sys.stderr)
                sys.exit(-1)
            desc = line[len(cue):].strip()
            continue

        if line[:len(att_cue)].lower() == att_cue:
            attachments.extend(line[len(cue):].strip().split())
            continue

        specline  = line.split()
        eid      = specline[0] if len(specline)>0 else None
        escore   = specline[1] if len(specline)>1 else 0
        eauto    = specline[2] if len(specline)>2 else 'auto'

        if len(specline)>3:
            print(f"Error: riga {i} di '{spec_compito}' mal formattata",file=sys.stderr)
            sys.exit(-1)

        try:
            escore = int(escore)
            assert escore>=0
        except:
            print(f"Error: riga {i} di '{spec_compito}', il punteggio deve essere un numero >=0",file=sys.stderr)
            sys.exit(-1)

        if eauto not in ['auto','manuale']:
            print(f"Error: riga {i} di '{spec_compito}' terzo argomento 'auto', 'manuale', o nessuna specifica",file=sys.stderr)
            sys.exit(-1)

        speclines.append((eid,escore,eauto))

    return speclines

def make_table(results, sortby='cognome'):
    """Compila una tabella con le informazioni degli studenti

    La tabella contiene le informazioni sugli studenti che hanno
    consegnato. Per ogni studente abbiamo la sua postazione, la sua
    matricola, l'esito dei test pubblici e segreti di ogni esercizio,
    il punteggio ottenuto, più colonne per inserire i voti manuali
    e quello totale.

    Parameters:
    -----------
    results:
        esito delle valutazioni, per ogni studente
    sortby:
        colonna rispetto alla quale ordinare i risultati

    Return:
    -------
    una tabella, rappresentata come lista di righe

    """

    N = len(esame_data) # numero dei test
    es_automatici = []
    es_manuali    = []

    #
    for i in range(N):
        if esame_data[i][2] == 'manuale':
            es_manuali.append(i)
        elif esame_data[i][2] == 'auto':
            es_automatici.append(i)
        else:
            pass

    columns = [
        'nome',
        'cognome',
        'matricola',
        'data',
        'aula',
        'pos',
        'matricola anon.',
        'voto',
        'score',
        ]

    # colonne degli esercizi a correzione manuale
    for i in es_manuali:
        columns.append(" es{} a mano ({} punti) ".format(i+1,esame_data[i][1]))

    columns += ["automatico","bonus"]  # colonne dei voti di programmazione

    # colonne dei risultati dei test degli esercizi di programmazione
    for i in es_automatici:
        columns.append(f"{i+1}p")
        columns.append(f"{i+1}s")

    # annotazioni
    columns.append("note")

    rows = []

    today=date.today()

    test_sizes = {}

    for student in results:

        score = compute_score(student)

        row = ['']*len(columns)
        row[columns.index("nome")]            = student.get("nome","")
        row[columns.index("cognome")]         = student.get("cognome","")
        row[columns.index("matricola")]       = student.get("matricola","")
        row[columns.index("matricola anon.")] = ''
        row[columns.index("aula")]            = student.get("aula","")
        row[columns.index("pos")]             = student.get("pos","")
        row[columns.index("note")]            = ''
        row[columns.index("data")]            = today.strftime("%d/%m/%Y")
        row[columns.index("voto")]            = ''
        row[columns.index("score")]           = ''
        row[columns.index("automatico")]      ='{0:02}'.format(score)
        row[columns.index("bonus")]           = '0'

        esito = student['esito']
        for i,pubres,secres in esito:

            if i not in es_automatici: continue

            pcol  = columns.index(f"{i+1}p")
            scol  = columns.index(f"{i+1}s")

            for t,idx in [(pubres,pcol),(secres,scol)]:
                if t['status'] == 'timeout':
                    row[idx] = 'T'
                elif t['status'] == 'executed':
                    row[idx] = str(t['failures'] + t['errors'])
                elif t['status'] == 'missing':
                    row[idx] = 'M'
                elif t['status'] == 'broken':
                    row[idx] = 'B'
                elif t['status'] == 'no test':
                    row[idx] = '-'
                else:
                    row[idx] = 'X'

                # Collect the total number of tests for the header
                # Only possible if tests are executable
                if idx not in test_sizes and 'total' in t:
                    test_sizes[idx] = t['total']

        rows.append(row)

    # numero di test totali nell'intestazione
    for i in test_sizes:
        size = test_sizes[i]
        columns[i] += ":{}".format(size)

    # anonimizza il campo matricola
    matricola_index=columns.index("matricola")
    anon_index=columns.index("matricola anon.")
    try:
        anon_ids = anonimize([row[matricola_index] for row in rows])
        for row in rows:
            row[anon_index] = anon_ids[row[matricola_index]]
    except ValueError:
        print(
            "WARNING: Impossibile anonimizzare. Matricole troppo simili o corte."
        )

    # sort by field f
    try:
        f = columns.index(sortby)
        if f >= 0:
            rows.sort(key=lambda x: x[f])
    except ValueError:
        print("WARNING: Impossibile ordinare per '{}'.".format(sortby))

    rows.insert(0, columns)
    return rows


# Piece of code stolen from
# https://stackoverflow.com/questions/7445658/how-to-detect-if-the-console-does-support-ansi-escape-codes-in-python
def supports_color():
    """
    Returns True if the running system's terminal supports color, and False
    otherwise.
    """
    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32'
                                                  or 'ANSICON' in os.environ)
    # isatty is not always implemented, #6223.
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    return supported_platform and is_a_tty


def report_on_screen(results):
    """Stampa a schermo l'esito del lavoro di un singolo studente.

    Parameters
    ----------
    results:
        tutte le informazioni riguardo all'esito degli esercizi per lo
        studente.
    """

    if supports_color():
        red = "\u001b[31m"
        green = "\u001b[32m"
        magenta = "\u001b[35m"
        cyan = "\u001b[36m"
        reset = "\u001b[0m"
    else:
        red = green = magenta = cyan = reset = ''

    basicinfo = """
Studente:  {nome} {cognome}
Matricola: {matricola}
Seduto in {aula} alla postazione {pos}\n""".format(**results)

    print(basicinfo)

    print("{:^20}{:^15}{:^15}{:^7}".format('', 'Test pubblici', 'Test privati',
                                           'Score'))

    esito = { i:(p,s) for (i,p,s) in results['esito']}
    appendix = ""

    for i in range(len(esame_data)):
        text = [None, None]
        name = esame_data[i][0]

        ex_entry  = "Esercizio " + str(i + 1)
        correzione  = esame_data[i][2]

        for j in [0, 1]:
            text[j] = esito[i][j]['status']

            if text[j] == 'timeout':
                text[j] = cyan + '{:^15}'.format('timeout') + reset
            elif text[j] == 'missing':
                text[j] = magenta + '{:^15}'.format('missing') + reset
            elif text[j] == 'broken':
                text[j] = magenta + '{:^15}'.format('broken') + reset
            elif text[j] == 'no test':
                text[j] = '{:^15}'.format('no test')
            else:
                F = esito[i][j]['failures']
                E = esito[i][j]['errors']
                T = esito[i][j]['total']

                if E + F == 0:
                    text[j] = green + '{:^15}'.format('{:2}/{} errori'.format(
                        0, T)) + reset
                else:
                    text[j] = red + '{:^15}'.format('{:2}/{} errori'.format(
                        E + F, T)) + reset

        if correzione == 'manuale':
            appendix = " + correzione manuale"
            ex_entry += " manuale"

        score = compute_exercise_score(i,esito[i][0],esito[i][1])

        print("{:<20}{}{}{:^7} {}".format(ex_entry, text[0],
                                              text[1], score, name))

    print("\nPUNTEGGIO FINALE: {}{}".format(compute_score(results),appendix))


def org_print_table(table, headers=True):
    """Stampa la tabella dei risultati come org-table

    Parameters:
    -----------
    table:
        tabella dei risultati degli studenti
    headers:
        la prima riga contiene le intestazioni
    """
    if len(table) == 0:
        return

    # Compute the widh of each column, as the maximum with of the data
    # in that column
    rowlen = len(table[0])
    column_width = [0] * rowlen
    fmt_str = [''] * rowlen
    for row in table:
        for i in range(rowlen):
            column_width[i] = max(column_width[i], len(row[i]))
    for i in range(rowlen):
        fmt_str[i] = ' {:>' + str(column_width[i]) + '} |'

    # Top row
    separator = "|" + '+'.join('-' * (column_width[i] + 2)
                               for i in range(rowlen)) + '|'
    print(separator)
    for ri in range(len(table)):
        row = table[ri]
        print("|", end='')
        for i in range(rowlen):
            print(fmt_str[i].format(row[i]), end='')
        print('')
        if ri == 0 and headers:
            print(separator)
    print(separator)


def csv_export(table, headers=True):
    """Stampa la tabella dei risultati in formato csv

    Parameters:
    -----------
    table:
        tabella dei risultati degli studenti
    headers:
        la prima riga contiene le intestazioni
    """
    writer = csv.writer(sys.stdout)
    for ri in range(len(table)):
        writer.writerow(table[ri])


def latex_doc(table, headers=True, rowsperpage=20):
    """Stampa la tabella dei risultati come file latex

    Parameters:
    -----------
    table:
        tabella dei risultati degli studenti
    headers:
        la prima riga contiene le intestazioni

    """
    print(r"""%
\documentclass[11pt]{article}
\usepackage{amsmath}
\usepackage[utf8]{inputenc}
\usepackage[table]{xcolor}

\begin{document}

\hoffset=-1in
\voffset=-1in

\rowcolors{2}{gray!15}{white}
""")

    # Create the table
    rowlen = len(table[0])
    rowidx = 1
    if headers:
        headernames = [' '] + [c.capitalize() for c in table[0]]
        datastart = 1
    else:
        datastart = 0

    tablefmt = "|r|" + 'r' * rowlen + "|"
    #print("\\begin{center}")
    for ri in range(datastart, len(table)):

        if ri % rowsperpage == datastart % rowsperpage:
            # need to open a table
            print(r'\setbox0\hbox{',end='')
            print("\\begin{{tabular}}{{{}}}".format(tablefmt))
            print("\\hline")
            if headers:
                print("\\rowcolor{gray!50}")
                print(" & ".join(headernames), end=' \\\\\n')
                print("\\hline")

        print(" ", rowidx, " & ", end='')
        print(" & ".join(table[ri]), end=' \\\\\n')
        rowidx += 1

        if ri % rowsperpage == (datastart - 1) % rowsperpage or ri == (
                len(table) - 1):
            print(r"""\hline
\end{tabular}}
\pdfpageheight=\dimexpr\ht0+\dp0\relax
\pdfpagewidth=\wd0
\shipout\box0""")

    print(r'\stop')

def make_pdf_file(table, pdffile):
    """Stampa la tabella in formato PDF

    Parameters:
    -----------
    table:
        tabella dei risultati degli studenti
    pdffile:
        nome del file pdf da produrre
    """
    originalwd = os.getcwd()
    tempdir = tempfile.mkdtemp()
    texfile = os.path.splitext(pdffile)[0] + os.path.extsep + 'tex'
    dstfile = os.path.join(originalwd, pdffile)
    srcfile = os.path.join(tempdir, pdffile)

    with working_dir(tempdir):
        # Prepara il sorgente latex
        with open(texfile, 'w', encoding='utf-8') as ostream:
            with redirect_stdout(ostream):
                latex_doc(table)

        # Compila se possibile
        subprocess.run([tex_cmd, texfile],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

    # Sposta il file nella destinazione prevista e pulisci la cartella
    # temporanea
    shutil.copyfile(srcfile, dstfile)
    shutil.rmtree(tempdir, ignore_errors=True)


def get_immediate_subdirectories():
    dirs = [
        name for name in os.listdir(os.path.curdir)
        if os.path.isdir(os.path.join(os.path.curdir, name))
    ]
    dirs.sort()
    return dirs


def in_student_directory():
    """Controlla se la cartella corrente è una cartella studenti.

    Controlla se il file 'studente.txt' è presente nella cartella
    corrente. Se sì allora restituisce True, e False altrimenti.

    Non verifica che il file contenga informazioni ben compilate.
    """
    return os.path.isfile(file_studente)


def in_exam_directory():
    """Controlla se la cartella corrente è una cartella esame.

    Controlla se il file 'esame.txt' è presente nella cartella
    corrente. Se sì allora restituisce True, e False altrimenti.

    Non verifica che il file contenga informazioni ben compilate.
    """
    return os.path.isfile(file_esame)


def parse_computer_folder(foldername):
    data = {}
    path = os.path.abspath(foldername)
    folder = os.path.basename(path)
    if folder[:3] in id_aule:
        data['aula'] = id_aule[folder[:3]]
    else:
        data['aula'] = "-"
    if folder[3:].isdigit():
        data['pos'] = folder[3:]
    else:
        data['pos'] = '-'

    return data

def add_default_email_address(data):
    if 'email' in data:
        return
    cognome=[c for c in data['cognome'] if c.isalpha() ]
    cognome=''.join(cognome)
    cognome=cognome.lower()
    email=cognome+"."+data['matricola']+"@studenti.uniroma1.it"
    data['email']=email

def scan_student_file(fobject):
    """Estrae le informazioni dello studente da un file

    Il file con le informazioni dello studente deve avere le righe

    nome: <nome>
    cognome: <cognome>
    matricola: <numerodimatricola>

    Altre righe verranno ignorate. In caso di righe multiple con la
    stessa informazione, verrà sollevato un errore.

    In caso di errori nell'accesso a file o nel formato del file
    verranno sollevati errori.

    Parameters
    ----------
    fobject
        file contentente le informazioni dello studente

    Return
    ------
    dizionario con le informazioni dello studente
    """
    data = {}
    requiredkeys = {'nome', 'cognome', 'matricola'}
    for line in fobject:
        # alcuni file hanno il Byte-Order-Marks
        line = line.replace('\ufeff', '')
        sep = line.find(':')
        if sep < 0:
            continue
        key, entry = line[:sep].strip().lower(), line[sep +
                                                      1:].strip().capitalize()

        if key not in requiredkeys:
            continue

        if key in data:
            raise ValueError('informazione \'{}\' duplicata'.format(key))

        if len(entry) == 0:
            fobject.seek(0)
            flines = [
                l.strip() for l in fobject.readlines() if len(l.strip()) != 0
            ]
            if flines == file_template:
                raise ValueError(
                    'file \'{}\' non compilato'.format(file_studente))
            raise ValueError('informazione \'{}\' assente'.format(key))

        data[key] = entry

    missingkeys = [x for x in requiredkeys if x not in data]
    if len(missingkeys):
        raise ValueError('mancano le informazioni {}'.format(missingkeys))

    return data


def matricole_ripetute(results):
    """Identifica le  matricole ripetute

    Identifica le matricole che occorrono più volte, fornendo il
    numero di ripetizioni in una lista di coppie
    (matricola,ripetizione), ordinata per matricola.
    """
    freq = {}
    for info in results:
        freq[info['matricola']] = freq.get(info['matricola'], 0) + 1
    result = [(k, v) for k, v in freq.items() if v > 1]
    return result


def extract_student_info():
    assert in_student_directory()

    # legge le informazioni dal file studente
    with open(file_studente, 'r') as f:
        info = scan_student_file(f)
        info['cartella'] = os.path.abspath(os.path.curdir)

    # trova il nome della cartella corrente ed in caso estrae
    # informazioni aggiuntive
    additional_info = parse_computer_folder(os.path.curdir)
    info.update(additional_info)

    return info


def decide_file_name(base, ext):

    filename = base + os.path.extsep + ext
    i = 0

    while os.path.isfile(filename):
        i += 1
        filename = base + str(i) + os.path.extsep + ext

    return filename

def compute_exercise_score(i,p,s):
    if esame_data[i][2] == 'manuale':
        return 0

    pgood = p['status'] == 'no test' or \
        p['status'] == 'executed' and \
        p['failures'] == 0 and \
        p['errors'] == 0

    sgood = s['status'] == 'no test' or \
        s['status'] == 'executed' and \
        s['failures'] == 0 and \
        s['errors'] == 0

    if pgood and sgood:
        return esame_data[i][1]
    else:
        return 0


def compute_score(info):
    total = 0
    for i,p,s in info['esito']:
        v = compute_exercise_score(i,p,s)
        if v is None: continue
        total += v
    return total


def info_sep(testo, length=40, fill='*', ostream=sys.stdout):
    print("INFO: " + fill * length)
    if len(testo) + 2 > length:
        print("INFO: " + testo, file=ostream)
    else:
        fmtstr = 'INFO: {{:{}^{}}}'.format(fill, length)
        print(fmtstr.format(" " + testo + " "), file=ostream)
    print("INFO: " + fill * length)


def anonimize(matricole):
    """Anonimizzazione delle matricole

    Data una lista di matricole senza ripetizioni, le anonimizza
    coprendo le cifre iniziali con asterischi, mantenendo
    alcune garanzie.

    - non ci sono due matricole anonimizzate uguali,

    - le matricole anonimizzare hanno tutte la stessa lunghezza, anche
      se questo non è vero per le matricole originali.

    Resituisce un dizionario (matricola -> matricola anonimizzata)

    Solleva ValueError se non è possibile anonimizzare le matricole,
    o se non è possibile farlo senza svelarne una completamente.

    """
    if len(matricole) == 0:
        return {}

    # Padding con spazi di fronte
    maxlength = max(len(x) for x in matricole)
    minlength = min(len(x) for x in matricole)
    # paia (matricola,anonimizzata)
    worklist = [' ' * (maxlength - len(x)) + x for x in matricole]

    for unveiled in range(0, minlength + 1):
        coversize = maxlength - unveiled
        coverlist = [('*' * coversize + x[coversize:], x) for x in worklist]
        coverlist.sort()

        # le matricole sono uniche?
        collision = False
        for i in range(len(coverlist) - 1):
            if coverlist[i][0] == coverlist[i + 1][0]:
                collision = True
                break
        # sì, sono uniche
        if not collision:
            res = {}
            for anon, orig in coverlist:
                res[orig.strip()] = anon
            return res

    raise ValueError("Impossibile anonimizzare ripetizioni.")


# Main program
def command_line_utility(argv=sys.argv):
    """Interfaccia a linea di comando del correttore

    Parameters
    ----------
    argv: list, optional
        The list of token with the command line arguments/options.
    """

    progname = os.path.basename(argv[0])
    parser = setup_command_line_parsers(progname)
    args = parser.parse_args(argv[1:])
    original_working_dir = os.getcwd()

    global esame_data, esame_path, esame_attachments

    # Controlla l'esistenza delle due cartelle
    error_mgs = []
    if not os.path.isdir(args.solutiondir):
        error_mgs.append("ERROR: la cartella {} non esiste".format(
            args.solutiondir))
    if not os.path.isdir(args.examdir):
        error_mgs.append("ERROR: la cartella {} non esiste".format(
            args.examdir))
    # Controlla l'esistenza dei comandi python3 e pdflatex
    if shutil.which(py_cmd) is None:
        error_mgs.append("ERROR: il comando '{}' non può essere eseguito. "
                         "Impossibile continuare.".format(py_cmd))

    # Controlla se il formato Excel è stato scelto
    # anche se manca il pachetto xlsxwriter e anche se non è ancora implementato
    if 'xlsx' in args.format:
        error_mgs.append("ERROR: l'output in formato 'xlsx' non è ancora disponibile")
        try:
            import xlsxwriter
        except ImportError:
            error_mgs.append("ERROR: formato 'xlsx' richiede il pacchetto 'xlsxwrite'")

    if len(error_mgs) > 0:
        for e in error_mgs:
            print(e, file=sys.stderr)
        sys.exit(-1)


    info_sep("Ambiente di esecuzione")
    print("INFO: Cartella esame    --- {}".format(os.path.abspath(
        args.examdir)))
    print("INFO: Cartella studenti --- {}".format(
        os.path.abspath(args.solutiondir)))

    if shutil.which(tex_cmd) is None:
        print("INFO: Formato PDF disabilitato: '{}' non può essere eseguito.".
              format(tex_cmd))
        if 'pdf' in args.format:
            args.format.remove('pdf')

    esame_path = os.path.abspath(args.examdir)

    # Estraiamo le specifiche dell'esame
    with working_dir(esame_path):
        if not in_exam_directory():
            print(
                "ERROR: la cartella {} non contiene le specifiche dell'esame".
                format(args.examdir),
                file=sys.stderr)
            sys.exit(-1)
        try:
            esame_data = estrazione_specifiche_compito(os.path.join(esame_path, file_esame))
            esame_attachments = allegati_compito(os.path.join(esame_path, file_esame))

            info_sep("Specifica dell'esame")
            for i, exspec in enumerate(esame_data, start=1):
                if exspec[2] == 'manuale':
                    print(f"INFO: Esercizio {i} - {exspec[0]:<24} - {exspec[1]:2} punti, correzione manuale")
                elif exspec[2] == 'auto':
                    print(f"INFO: Esercizio {i} - {exspec[0]:<24} - {exspec[1]:2} punti")
                else:
                    print("ERROR: '{}' contiene informazioni non coerenti".format(esame_path), file=sys.stderr)
                    sys.exit(-1)
            for f in esame_attachments:
                if not os.path.isfile(f):
                    raise ValueError(f'ERROR: allegato {f} non trovato')
                print("INFO: ATTACHMENT>",f,file=sys.stderr)

        except Exception as e:
            print("ERROR: '{}' {}".format(esame_path, str(e)), file=sys.stderr)
            sys.exit(-1)

    # Andiamo nella cartella delle soluzioni
    os.chdir(args.solutiondir)

    # Quali sottocartelle devono essere scansionate?
    single_student = False
    folder_list = []
    if in_student_directory():
        single_student = True
        if args.scan:
            info_sep("Scansione di un solo studente")
        else:
            info_sep("Correzione di un solo studente")
        folder_list.append(os.path.abspath(os.path.curdir))
    else:
        if args.scan:
            info_sep("Scansione degli studenti")
        else:
            info_sep("Correzione degli studenti")
            if len(args.format) == 0:
                print("ERROR: nessun formato specificato per i report.",
                      file=sys.stderr)
                sys.exit(-1)
            print("INFO: Saranno prodotti report nei formati " +
                  ', '.join(args.format) + ".")

        for subdir in get_immediate_subdirectories():
            folder_list.append(os.path.abspath(subdir))

    # Eseguiamo la scansione e l'esecuzione dei test per
    # ogni studente.
    results = []
    for subdir in folder_list:
        with working_dir(subdir):
            valid_info = True
            error = None
            try:
                info = extract_student_info()
            except Exception as e:
                valid_info = False
                error = str(e)
                info = {'nome':'-',
                        'cognome':'-',
                        'matricola':'-',
                        'pos':'-',
                        'aula':'-'}

            if not (valid_info or single_student):
                # Non ci sono info per lo studente. Accettabile solo in modalità
                # correzione singola
                subdirname = os.path.basename(subdir)
                print('INFO: \'{}\' scartata --- {}'.format(
                    subdirname, error))
                continue

            print('INFO: Consegna di {nome} {cognome} alla'
                  ' postazione {pos} ({aula})'.format(**info))

            if not args.scan:
                esito = execute_test_for_student()
                info['esito'] = esito
                if args.errors:
                    errortext=StringIO()
                    print(esito)
                    for i,a,b in esito:
                        if 'stderr' in a:
                            errortext.write(a['stderr'])
                        if 'stderr' in b:
                            errortext.write(b['stderr'])
                    info['stderr'] = errortext.getvalue()
            results.append(info)


    # Terminata la scansione, dobbiamo fare altro?
    os.chdir(original_working_dir)

    if args.scan:
        info_sep("Trovate {:>3} consegne".format(len(results)))
        sys.exit(0)

    # Se siamo in una cartella studente il report è al terminale.
    if single_student:
        assert len(results)>0
        report_on_screen(results[0])
        if args.errors:
            print("Stderr:")
            print(results[0]['stderr'])
        sys.exit(0)

    # Costruiamo i report: la variabile 'results' contiene tutti
    # i dati degli studenti e l'esito dei loro esercizi. I dati
    # vengono messi in una tabella che viene formattata e salvata su
    # file di vari tipi.
    if len(results) == 0:
        info_sep("Non ci sono compiti consegnati")
        sys.exit(0)

    info_sep("Report per {:>3} studenti".format(len(results)))
    print("INFO: Ordina rispetto al campo '{}'".format(args.rankby))

    repeated = matricole_ripetute(results)
    for m, t in repeated:
        print("WARNING: la matricola '{}' occorre {} volte.".format(m, t))

    table = make_table(results,
                       sortby=args.rankby.lower())

    formatters = {
        'xls': None,
        'org': org_print_table,
        'csv': csv_export,
        'tex': latex_doc,
        'pdf': make_pdf_file
    }

    for ext in args.format:

        if ext not in formatters:
            print('INFO: Output in {} format not yet implements'.format(
                ext.upper()))
            continue

        filename = decide_file_name(args.output, ext)

        print('INFO: Output in {} format \'{}\''.format(ext.upper(), filename))

        if ext == 'pdf':
            # PDF output richiede del lavoro aggiuntivo
            make_pdf_file(table, filename)
        else:
            with open(filename, 'w', encoding='utf-8') as ostream:
                with redirect_stdout(ostream):
                    formatters[ext](table)


# command line entry point
if __name__ == '__main__':
    command_line_utility(sys.argv)
