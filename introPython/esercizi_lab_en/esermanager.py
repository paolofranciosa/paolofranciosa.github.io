#!/usr/bin/env python3

import os
import sys
import json
import base64
import shutil
import subprocess
from contextlib import contextmanager
from datetime import datetime
from sys import stderr

TEMPLATE="TEST_TEMPLATE.py"
ST='# ------ START TEST SECTION ------\n'
ET='# ------ END   TEST SECTION ------\n'

PREAMBOLO="PREAMBOLO.md"
TAVOLA_SINOTTICA="sintassi_python.pdf"
CORRETTORE="correttore.py"
INFO_STUDENTE="studente.txt"
SPEC_ESAME='esame.txt'
ARCHIVIO_DIST="Archivio-Da-Distribuire.zip"

# Folders in the repo
REPO_ASSETS="assets"
REPO_SUBDIRS=[".",
              "tools",
              "esercizi_lab","esercizi_esame","esercizi_esame_toreview"]


def get_repo_path():
    # Find git
    scriptdir = os.path.dirname(os.path.abspath(sys.argv[0]))
    oldwd = os.getcwd()
    try:
        os.chdir(scriptdir)
        repo_dir = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'],
                                    stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')
    except:
        print(f"Error: impossibile la root del repository dello script",file=sys.stderr)
        sys.exit(-1)
    finally:
        os.chdir(oldwd)

    return os.path.abspath(repo_dir)

def list_titoli():
    """Elenca gli esercizi installati"""

    repo_dir = get_repo_path()

    lines = []

    for subdir in REPO_SUBDIRS:

        location = repo_dir +"/" + subdir +"/"
        if not os.path.isdir(os.path.abspath(location)): continue

        for f in os.listdir(os.path.abspath(location)):
            if not f.endswith(".ipynb"): continue
            size = 30
            title = ''
            fname     = os.path.basename(f)
            trunc = ('...'+fname[-size:]) if len(fname) > (size+3) else fname
            with open(location+f, 'r') as notebook:
                cells = json.load(notebook)['cells']
            for c in cells:
                H = markdown_headers(c)
                if len(H) > 0:
                    title=H[0]
                    break
            flags = [' ',' ',' ',' ']
            try:
                extract_section_code('test segreti',cells)
                flags[3] = 'S'
            except ValueError:
                pass
            try:
                extract_section_code('test pubblici',cells)
                flags[2] = 'P'
            except ValueError:
                pass
            try:
                extract_section_code('implementazione',cells)
                flags[1] = 'I'
            except ValueError:
                pass
            try:
                extract_section_markdown('traccia',cells,None)
                flags[0] = 'T'
            except ValueError:
                pass

            lines.append("{:<30} {} {}".format(trunc,"".join(flags),title))

    for l in sorted(lines):
        print(l)

def trova_file(pathname,isdir=False):
    """Cerca un file, nell'ordine:
    - nella cartella corrente
    - relativamente alla root del repository
      git che contiene questo script (se applicabile)
    """
    if isdir:
        checkfunc = os.path.isdir
    else:
        checkfunc = os.path.isfile

    # current dir
    if checkfunc(pathname):
        return os.path.abspath(pathname)

    repo_dir = get_repo_path()

    for subdir in REPO_SUBDIRS:
        location = repo_dir +"/" + subdir +"/"+pathname
        if checkfunc(location):
            return os.path.abspath(location)
    print(f"Error: impossibile trovare {pathname}",file=sys.stderr)
    sys.exit(-1)

def copy_if_needed(src,dst):
    if os.path.abspath(src) == os.path.abspath(dst):
        return
    else:
        shutil.copyfile(src,dst)


def convert_and_remove(inputfile,outputfile,options=""):
    clitool='pandoc'
    options=options.split()
    if shutil.which(clitool) is None:
        return False
    subprocess.run([clitool, inputfile]+ options + ['-o',outputfile],
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    if not os.path.isfile(outputfile):
        return False
    os.remove(inputfile)
    return True


def markdown_headers(cell):
    if cell['cell_type']!='markdown': return []

    H=[]
    for line in cell['source']:
        if line[0]!='#': continue
        i=0
        while line[i]=='#': i+=1
        H.append(line[i:].strip())
    return H



def extract_section_markdown(title,cells,img_fname=None):
    ltitle = title.lower()
    data=[]
    in_section = False
    img_cnt = 0
    for c in cells:

        # code to be copied
        if c['cell_type']=='code':
            if in_section:
                data.append('\n```{.python}\n')
                data.extend(c['source'][:])
                data.append('\n```\n')

                for out in c['outputs']:
                    if out['output_type']=="execute_result":
                        try:
                            outdata= out['data']['text/plain'][:]
                            data.append('\n```\n')
                            data.extend(outdata)
                            data.append('\n```\n')
                        except KeyError:
                            pass
                    elif out['output_type']=="stream":
                        try:
                            data.append('\n```\n')
                            data.extend(out['text'])
                            data.append('\n```\n')
                        except KeyError:
                            pass
                    elif out['output_type']=="display_data":
                        if img_fname is None:
                            continue
                        try:
                            # save image to file
                            img_data = out['data']['image/png'].encode('ascii')
                            img_text = out['data']['text/plain']
                            img_cnt += 1
                            img_outfile = img_fname.format(img_cnt)
                            with open(img_outfile, "wb") as fh:
                                fh.write(base64.decodebytes(img_data))
                            # include it into markdown
                            data.append("\n")
                            data.append(f"![{img_text}]({img_outfile})")
                            data.append("\n")
                        except KeyError:
                            pass

            continue

        # not code not markdown
        if c['cell_type']!='markdown': continue

        # text to be copied
        for line in c['source']:
            # found header?
            if len(line)>0 and line[0]=='#' and not in_section:
                i=0
                while line[i]=='#': i+=1
                sectitle = line[i:].strip().lower()
                in_section = ltitle == sectitle
            elif len(line)>0 and line[0]=='#' and in_section:
                return ''.join(data)
            elif in_section:
                data.append(line)

    if not in_section:
        raise ValueError('No section titled \''+title+'\'')
    return ''.join(data)

def extract_section_code(title,cells):
    ltitle = title.lower().strip()
    data=[]
    in_section = False
    for c in cells:

        # file content?
        if get_file_content(c) is not None:
            continue

        # code to be copied (exclude shell command lines)
        if c['cell_type']=='code':
            if in_section:
                for line in c['source']:
                    x = line.strip()
                    if len(x)>0 and x[0]=="!": continue #shell command
                    data.extend(line)
            continue

        # not code not markdown
        if c['cell_type']!='markdown': continue

        # check the section
        for line in c['source']:
            # found header?
            if len(line)>0 and line[0]=='#' and not in_section:
                i=0
                while line[i]=='#': i+=1
                sectitle = line[i:].strip().lower()
                in_section = ltitle == sectitle
            elif len(line)>0 and line[0]=='#' and in_section:
                return ''.join(data)
    if not in_section:
        raise ValueError('No section titled \''+title+'\'')
    return ''.join(data)


def test_blocks():
    with open(TEMPLATE,'r') as f:
        lines = f.readlines()
    for i,l in enumerate(lines):
        if ST==l:
            break
    return "".join(lines[:i+1]),"".join(lines[i+1:])

def get_file_content(cell):
    if cell['cell_type']!='code': return None
    i = 0
    lines = cell['source']
    while i<len(lines) and len(lines[i].strip())==0:
        i+=1
    if i==len(lines): return None
    spec = lines[i].split()
    if spec[0]=="%%file":
        return spec[1],"".join(lines[i+1:])
    else:
        return None

def extract_files(cells):
    files = []
    for c in cells:
        data  = get_file_content(c)
        if data is not None:
            files.append(data)
    return files

# Estrazione del singolo esercizio
def estrazione_esercizio(ex_file_name, formato_traccia="md",score=None):
    """Interfaccia a linea di comando del correttore
    """
    ex_name = os.path.basename(ex_file_name)
    ex_name = os.path.splitext(ex_name)[0]
    ex_title=''
    ex_attachments=[]

    with open(ex_file_name, 'r') as ex_file:
         cells = json.load(ex_file)['cells']

    print(f"* Esercizio '{ex_name}' ({os.path.abspath(ex_file_name)})",file=sys.stderr)

    # Titolo dell'esercizio
    for c in cells:
        H = markdown_headers(c)
        if len(H) >= 0:
            ex_title=H[0]
            break

    print(f"  - titolo: ",end="",file=sys.stderr)
    if len(ex_title)==0:
        ex_title = "titolo indefinito"
    if score is not None:
        ex_title += f" ({score} points)"
    print(ex_title,file=sys.stderr)


    # Scheletro del file di test
    top,bottom = test_blocks()

    pub , pri, impl = None, None, None

    # Test pubblici
    print(f"  - test pubblici: ",end="",file=sys.stderr)
    try:
        pub = extract_section_code('Test pubblici',cells)
    except ValueError:
        print("non trovati",file=sys.stderr)
    else:
        with open('test_'+ex_name+".py","w") as out:
            print(top,file=out)
            print(pub,file=out)
            print(bottom,file=out)
        print('test_'+ex_name+".py",file=sys.stderr)

    # Test segreti
    print(f"  - test segreti : ",end="",file=sys.stderr)
    try:
        pri = extract_section_code('Test segreti',cells)
    except ValueError:
        print("non trovati",file=stderr)
    else:
        with open('test_'+ex_name+"_secret.py","w") as out:
            print(top,file=out)
            print(pri,file=out)
            print(bottom,file=out)
        print('test_'+ex_name+"_secret.py",file=sys.stderr)

    # Implementazione
    print(f"  - implementazione: ",end="",file=sys.stderr)
    try:
        impl = extract_section_code('Implementazione',cells)
    except ValueError:
        print("non trovata",file=sys.stderr)
    else:
        with open(ex_name+".py","w") as out:
            print(impl,file=out)
        print(ex_name+".py",file=sys.stderr)

    # File allegati
    file_list = extract_files(cells)
    for fname,content in file_list:
            print(f"  - file allegato: {fname}",file=sys.stderr)
            with open(fname,"w") as attachment_out:
                attachment_out.write(content)
            ex_attachments.append(fname)

    # Traccia
    print(f"  - traccia: ",end="",file=sys.stderr)
    try:
        traccia = extract_section_markdown('traccia',cells,None)
    except ValueError:
        print("non trovata",file=stderr)
    else:
        with open(ex_name+".md","w") as out:
            print('# '+ex_title,file=out)
            print(extract_section_markdown('traccia',cells,
                                           "./imgtmp/"+ex_name+"_{:02}.png"),
                  file=out)
            print("\n",file=out)
            if impl is not None:
                print("\nPython function must be "+
                      "saved in file: `"+ex_name+".py`", file=out)
            if pub is not None:
                print("\nTest file: `test_"+ex_name+".py`",file=out)
        if formato_traccia!='md':
            conversione_riuscita=convert_and_remove(ex_name+".md",ex_name+"."+formato_traccia)
        else:
            conversione_riuscita=True
        if conversione_riuscita:
            print(ex_name+"."+formato_traccia,file=sys.stderr)
        else:
            print(ex_name+".md (conversione fallita)",file=sys.stderr)
    return ex_title,ex_attachments


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

    """


    basename = os.path.basename(spec_compito)

    compito={
        "file"        : os.path.splitext(basename)[0],
        "titolo"      : None,
        "tracce"      : [],
        "ids"         : [],
        "scores"      : [],
        "titoli"      : [],
        "correzione"  : [],
        "allegati"    : []
    }

    cue="descrizione:"
    attcue="allegati:"
    with open(spec_compito) as spec:
        lines=spec.readlines()
    desc = None
    speclines=[]
    for i,line in enumerate(lines,start=1):

        line=line.strip()

        if len(line)==0: continue

        if line.lower().startswith(cue):
            if desc is not None:
                print("Error: il file del compito ha più di una descrizione...",file=sys.stderr)
                sys.exit(-1)
            desc = line[len(cue):].strip()
            continue

        if line.lower().startswith(attcue):
            t = line.split()
            compito['allegati'].extend(t[1:])
            continue

        specline = line.split()
        eid    = specline[0] if len(specline)>0 else None
        escore = specline[1] if len(specline)>1 else None
        eauto  = specline[2] if len(specline)>2 else None

        if len(specline)>3:
            print(f"Error: riga {i} di '{spec_compito}' mal formattata",file=sys.stderr)
            sys.exit(-1)

        if escore is not None:
            try:
                escore = int(escore)
            except:
                print(f"Error: riga {i} di '{spec_compito}', il punteggio deve essere un numero >=0",file=sys.stderr)
                sys.exit(-1)

        if eauto not in ['auto','manuale'] and eauto is not None:
            print(f"Error: riga {i} di '{spec_compito}' terzo argomento 'auto', 'manuale', o nulla",file=sys.stderr)
            sys.exit(-1)

        # defaults
        if escore is None:
            eauto = 'nessuna'
        elif eauto is None:
            eauto = 'auto'

        speclines.append((eid,escore,eauto))

    compito['titolo'] = desc

    # Allegati non inseriti in esercizi
    if len(compito['allegati'])>=0:
        print(f'Allegati generici:',file=sys.stderr)
        for a in compito['allegati']:
            print(f' - {a}')

    for eid,escore,eauto in speclines:
        nbfile = trova_file(eid + ".ipynb")
        title, attachments = estrazione_esercizio(nbfile,score=escore)
        compito['tracce'].append(eid + ".md")
        compito['ids'].append(eid)
        compito['scores'].append(escore)
        compito['titoli'].append(title)
        compito['correzione'].append(eauto)
        compito['allegati'].extend(attachments)
    return compito


def tabellaorgmode(compito):
    print(f"* Tabella org-mode del compito {compito['file']}.pdf on stdout",
          file=sys.stderr)
    print(f"  Esercitazione da fare in laboratorio: [[file:esercizi/{compito['file']}.pdf][scarica]].")
    print("""
    |------------------------+-------------------------------|
    | Esercizio              | file di test                  |
    |------------------------+-------------------------------|""")
    for titolo,eid in zip(compito['titoli'],compito['ids']):
        if os.path.isfile(f"test_{eid}.py"):
            print(f"    | {titolo} | [[file:esercizi/test_{eid}.py][test_{eid}.py]] |")
    if len(compito['allegati'])>0:
        print("    |------------------------+-------------------------------|")
    for allegato in compito['allegati']:
        print(f"    | Allegato | [[file:esercizi/{allegato}][{allegato}]] |")
    print("    |------------------------+-------------------------------|")
    print("""
  Man mano che  lavorate sui vostri esercizi potete  testare le vostre
  soluzioni eseguendo i file di test corrispondenti.""")

def composizione_compito(compito,output_format='pdf'):

    print(f"* Creazione del compito {compito['file']}.{output_format} con titolo:\n    {compito['titolo']}",
          file=sys.stderr)
    with open(compito['file']+".md","w") as out:
        anno=datetime.now().year
        currdate = (datetime.now().month,
                    datetime.now().day)
        if currdate > (9,14):   # later than september 10th?
            yearstring=f"({anno}/{anno+1})"
        else:
            yearstring=f"({anno-1}/{anno})"

        datestring=compito['titolo']
        with open(PREAMBOLO) as f:
            preamble = f.readlines()
        # Interpolate only the first 5 lines
        for i,pline in enumerate(preamble):
            if i<5:
                pline=pline.format(yearstring=yearstring,
                                   description=compito['titolo'])
            print(pline,end="",file=out)
        print("\n\n",file=out)
        for tf in compito['tracce']:
            print("\\pagebreak",file=out)
            with open(tf) as f:
                print(f.read(),file=out)
            os.remove(tf)
    if output_format=='pdf':
        assets = trova_file(REPO_ASSETS,isdir=True)
        subprocess.run(['ln', '-s', assets, "." ],
                       stdout=subprocess.PIPE)
        convert_and_remove(compito['file']+".md",
                           compito['file']+".pdf",options="--highlight-style tango")
        assert os.path.islink(REPO_ASSETS)
        os.remove(REPO_ASSETS)
    elif output_format=='tex':
        convert_and_remove(compito['file']+".md",
                           compito['file']+".tex")
    elif output_format=='org':
        convert_and_remove(compito['file']+".md",
                           compito['file']+".org")
    elif output_format=='html':
        convert_and_remove(compito['file']+".md",
                           compito['file']+".html")
    elif output_format=='md':
        pass
    else:
        raise ValueError("invalid output_format")


    print("* File addizionali",file=sys.stderr)
    global TAVOLA_SINOTTICA,INFO_STUDENTE,CORRETTORE
    TAVOLA_SINOTTICA = trova_file(TAVOLA_SINOTTICA)
    INFO_STUDENTE = trova_file(INFO_STUDENTE)
    CORRETTORE = trova_file(CORRETTORE)
    print(f"  - tavola sinottica della sintassi python:  {TAVOLA_SINOTTICA}",file=sys.stderr)
    print(f"  - file per le informazioni dello studente: {INFO_STUDENTE}",file=sys.stderr)
    print(f"  - programma la correzione: {CORRETTORE}",file=sys.stderr)
    copy_if_needed(TAVOLA_SINOTTICA,os.path.basename(TAVOLA_SINOTTICA))
    copy_if_needed(INFO_STUDENTE,os.path.basename(INFO_STUDENTE))
    copy_if_needed(CORRETTORE,os.path.basename(CORRETTORE))
    shutil.os.chmod(os.path.basename(CORRETTORE),mode=0o755)
    print(f"  - file con le specifiche per l'esame, per il correttore: {SPEC_ESAME}",file=sys.stderr)
    shutil.copyfile(compito['file']+".txt",SPEC_ESAME)
    # scrivi gli allegati nel file esame.txt
    with open(SPEC_ESAME,'a') as se:
        se.write("allegati: "+ " ".join(compito['allegati']))

    # Archivio da distribuire
    print(f"* Archivio da distribuire: {ARCHIVIO_DIST}",file=sys.stderr)
    distribuiti = []
    distribuiti.append(os.path.basename(INFO_STUDENTE))
    distribuiti.append(os.path.basename(TAVOLA_SINOTTICA))
    for ex in compito['ids']:
        if os.path.isfile("test_"+ex+".py"):
            distribuiti.append("test_"+ex+".py")
    for allegato in compito['allegati']:
        if not os.path.isfile(allegato): continue
        if os.path.splitext(allegato)[0].endswith('_secret'): continue
        distribuiti.append(allegato)
    distribuiti.append(compito['file']+".pdf")
    for fn in distribuiti:
        print(f"  - {fn}",file=sys.stderr)
    if os.path.isfile(ARCHIVIO_DIST):
        os.remove(ARCHIVIO_DIST)
    subprocess.run(['zip', ARCHIVIO_DIST]+distribuiti,
                   stdout=subprocess.PIPE)
    print("OK",file=sys.stderr)

# usage string and documentation
usage_string="""
Usage:
  {0} file.txt        --- costruisci un compito (default: pdf)
  {0} file.ipynb      --- estrai i dati dal notebook (default: markdown)
  {0} -l|--list       --- elenca gli esercizi coi titoli

Si può impostare il formato di output  altenativo
  --html
  --org
  --tex
  --md

  -h|--help   mostra istruzioni d'uso

La specifica di un compito segue uno schema del tipo

--------
descrizione: Appello del 12 Gennaio 2054
dueminimi
satsolver  8
kclique    8 manuale
halting    10 auto
conteggioconsonanti 4
--------

- ogni esercizio ha opzionalmente un punteggio
- gli esercizi con punteggio possono avere la correzione
  automatica (default) o manuale.
"""



# command line entry point
if __name__ == '__main__':
    progname = os.path.basename(sys.argv[0])
    args = sys.argv[1:]
    valid_opts=["--help","-h","--org","--html","--md","--tex","--table"]

    # Usage string
    if "-h" in args or "--help" in args:
        print(usage_string.format(sys.argv[0]),file=sys.stderr)
        sys.exit(0)

    # Elenca esercizi
    if "-l" in args or "--list" in args:
        if len(args)!=1:
            print(usage_string.format(sys.argv[0]),file=sys.stderr)
            sys.exit(-1)
        list_titoli()
        sys.exit(0)

    # File come argomento nella riga di comando
    if len(args)==0:
        print(usage_string.format(sys.argv[0]),file=sys.stderr)
        sys.exit(-1)

    inputfile=args[-1]
    multi_file=True
    if inputfile[-6:]==".ipynb":
        multi_file = False
    elif inputfile[-5:]==".txt":
        multi_file = True

    fmt_opts = [o for o in ["org","html","md","tex"] if "--"+o in args]
    if len(fmt_opts)>1:
        print("Error: --org, --html, --md, --tex sono mutuamente esclusive. Usa --help per maggiori info.",file=sys.stderr)
        sys.exit(-1)

    # Check that only valid options are used
    for opt in args:
        if "-" == opt[0] and opt not in valid_opts:
            print("Error: opzione {} non valida. Usa --help per maggiori info.".format(opt),file=sys.stderr)
            sys.exit(-1)

    # Output format only in a single file process
    # if multi_file and ("--org" in args or "--html" in args):
    #     print("Error: il formato di output si può scegliere solo su un singolo notebook",file=sys.stderr)
    #     sys.exit(-1)

    if not multi_file and ("--tab" in args):
        print("Error: la tablella orgmode si può produrre solo per le esercitazioni",file=sys.stderr)
        sys.exit(-1)

    if "--org" in args:
        output_format = "org"
    elif "--html" in args:
        output_format = "html"
    elif "--tex" in args:
        output_format = "tex"
    elif "--md" in args:
        output_format = "md"
    else:
        output_format = 'pdf' if multi_file else 'md'

    TEMPLATE=trova_file(TEMPLATE)
    PREAMBOLO=trova_file(PREAMBOLO)
    print(f"Cartella di lavoro: {os.getcwd()}",file=sys.stderr)
    print(f"Preambolo il documento: trovato in '{os.path.abspath(PREAMBOLO)}'",file=sys.stderr)
    print(f"File template per test: trovato in '{os.path.abspath(TEMPLATE)}'",file=sys.stderr)
    if multi_file:
        cinfo = estrazione_specifiche_compito(inputfile)
        if "--table" in args:
            tabellaorgmode(cinfo)
        composizione_compito(cinfo,output_format=output_format)
    else:
        estrazione_esercizio(inputfile,formato_traccia=output_format)
