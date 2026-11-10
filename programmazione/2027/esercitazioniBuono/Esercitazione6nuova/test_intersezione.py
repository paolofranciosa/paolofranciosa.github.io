#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019, 2020, 2021, 2023, 2024 by Massimo Lauria <massimo.lauria@uniroma1.it>
"""Test per gli esercizi di informatica

Questo è un template per costruire i test per gli esercizi e gli esami
del corso di informatica del Dipartimento di Scienze Statistiche.
"""

import importlib
import unittest
import sys
import os
from collections import namedtuple
from copy import deepcopy


class TcUndef:
    pass


Testcase = namedtuple(
    'Testcase', " name fname fvalue input "
    " result error inplace "
    " explanation")
Testcase.__new__.__defaults__ = (TcUndef, ) * len(Testcase._fields)


def load_solution_file(filename_woext, functions):
    """Carica il file delle soluzioni

    Importa il modulo `filename_woext`, assumendo che sia nella
    cartella corrente, e da esse carica le funzioni elencate
    `functions` nel global namespace.

    Parameters
    ----------
    filename_woext : str
        Nome del modulo da caricare (senza estensione .py)

    functions: str or list(str)
        Lista di nomi di funzione da caricare nel modulo.
        Se l'argomento non è una lista ma una stringa, viene
        interpretata come una lista che contiene quel nome come
        unico elemento.

    """
    assert isinstance(filename_woext, str)

    if isinstance(functions, str):
        functions = [functions]

    for s in functions:
        assert isinstance(s, str)

    lab = None
    try:
        lab = importlib.__import__(filename_woext)
    except Exception:
        # File non importabile:
        print(f"ERRORE: Impossibile importare/eseguire {filename_woext}.py",file=sys.stderr)
        print(f"",file=sys.stderr)
        print(f"SUGGERIMENTI:",file=sys.stderr)
        print(f"    - {filename_woext}.py contiene errori di sintassi?",file=sys.stderr)
        print(f"    - prova ad eseguire il comando: python3 {filename_woext}.py",file=sys.stderr)
        print(f"    - prova ad eseguire il comando: python3 -c 'import {filename_woext}'",file=sys.stderr)
        sys.exit(-1)

    # Carica nel namespace le funzioni definite
    f_objects = {}
    try:
        for f_name in functions:
            f_object = lab.__dict__[f_name]
            f_objects[f_name] = f_object
    except KeyError:
        print(f"ERRORE: {filename_woext}.py non contiene la soluzione dell'esercizio",file=sys.stderr)
        print(f"",file=sys.stderr)
        print(f"SUGGERIMENTI:",file=sys.stderr)
        for f_name in functions:
            print(f"    - {filename_woext}.py contiene la funzione '{f_name}'?",file=sys.stderr)
            print(f"    - il nome della la funzione '{f_name}' è scritto correttamente?",file=sys.stderr)
        sys.exit(-1)

    globals().update(f_objects)

def error_msg(testcase, computed=TcUndef, backup=TcUndef):

    # Stringa che rappresenta la chiamata a funzione
    if testcase.inplace is not TcUndef:
        argstring = [repr(x) for x in backup]
    else:
        argstring = [repr(x) for x in testcase.input]
    argstring = ", ".join(argstring)
    callstring = testcase.fname+'('+argstring+')'

    messaggio = f"\n\nSPIEGAZIONE DELL'ERRORE:\n{callstring}\n"

    if testcase.result is not TcUndef:
        messaggio += f"    - ha restituito {repr(computed)}\n    - ma avrebbe dovuto restituire {repr(testcase.result)}"

    elif testcase.inplace is not TcUndef and len(testcase.input)==1:
        messaggio += f"    - ha modificato l'argomento ottenendo {repr(testcase.input[0])}\n    - ma avrebbe dovuto ottenere {repr(testcase.inplace[0])}"

    elif testcase.inplace is not TcUndef and len(testcase.input)>1:
        messaggio += f"    - ha modificato gli argomenti ottenendo {repr(testcase.input)}\n    - ma avrebbe dovuto ottenere {repr(testcase.inplace)}"

    elif testcase.error is not TcUndef:
        messaggio += f"    - avrebbe dovuto sollevare l'errore {testcase.error.__name__}"

    if testcase.explanation is not TcUndef:
        messaggio += "\n\n"+testcase.explanation

    return messaggio


def generate_test_function(testcase):

    if testcase.fname is TcUndef or testcase.fvalue is TcUndef:
        raise AttributeError("'{}' non contiene i campi 'fname' e 'fvalue', "
                             "che sono necessario.".format(testcase.name))

    if testcase.input is TcUndef:
        raise AttributeError(
            "'{}' non contiene il campo 'input', che è necessario.".format(
                testcase.name))

    # Checking that only one field among 'result', 'error', 'inplace'
    # is defined.
    behaviours = 0
    if testcase.result is not TcUndef:
        behaviours += 1
    if testcase.error is not TcUndef:
        behaviours += 1
    if testcase.inplace is not TcUndef:
        behaviours += 1

    if behaviours != 1:
        raise AttributeError("'{}' deve avere esattamente un campo tra "
                             "'result', 'error', 'inplace'.".format(
                                 testcase.name))

    if testcase.result is not TcUndef:
        # Test whether result is correct
        def tmp_test_function(self):
            func = testcase.fvalue
            computed = func(*testcase.input)  # executes the test
            msg = error_msg(testcase, computed)

            if testcase.result is None:
                self.assertIsNone(computed, msg=msg)
            else:
                self.assertEqual(testcase.result, computed, msg=msg)

    elif testcase.inplace is not TcUndef:
        # Test whether input was modified appropriately
        def tmp_test_function(self):

            func = testcase.fvalue
            input_backup = deepcopy(testcase.input)
            func(*testcase.input)  # executes the test
            msg = error_msg(testcase, backup=input_backup)

            self.assertEqual(testcase.inplace, testcase.input, msg=msg)

    elif testcase.error is not TcUndef:
        # Test for error signaling
        def tmp_test_function(self):

            func = testcase.fvalue
            msg = error_msg(testcase)

            with self.assertRaises(testcase.error, msg=msg):
                func(*testcase.input)  # executes the test
    else:
        raise RuntimeError("'{}' non saremmo dovuti arrivare qui!!!".format(
            testcase.name))

    return tmp_test_function


def build_test_class(testcases, func):
    """Crea la classe che contiene i test

    La suite di test di unità di Python esegue i test che
    corrispondono ai metodi test_* trovati nelle classi che ereditano
    da `unittest.TestCase`.

    Questa funzione crea una classe con queste caratteristiche

    Parameters
    ----------
    testcases: list(Testcase)
        Lista dei casi di test da caricare.

    func: function
        funzione da testare, quando non specificata dai casi di test.

    Returns
    -------
    unittest.TestCase
    """

    if hasattr(func,'__name__'):
        fname = func.__name__
    else:
        fname = 'anonymous_func'

    # Inseriamo la funzione da testare e il suo nome, in ogni test
    for i in range(len(testcases)):
        tc = testcases[i]
        if tc.fname is TcUndef:
            testcases[i] = tc._replace(fname=fname)
        tc = testcases[i]
        if tc.fvalue is TcUndef:
            testcases[i] = tc._replace(fvalue=func)


    mtestclass = type('TestTmp',(unittest.TestCase,),{})

    errori_nei_test = []

    for i, testcase in enumerate(testcases, start=1):
        try:
            if testcase.name is TcUndef:
                raise AttributeError(
                    "il test non contiene il campo 'name', che è necessario"
                    )

            test_name = 'test_' + "".join(testcase.name.split())
            if hasattr(mtestclass, test_name):
                raise ValueError("nome del metodo di test '{}' è duplicato".format(test_name))

            setattr(mtestclass, test_name, generate_test_function(testcase))

        except (ValueError, AttributeError) as err:
            errori_nei_test.append((i, err))

    if len(errori_nei_test) > 0:
        print("ERRORE NEI CASI DI TEST:")
        for i, err in errori_nei_test:
            print("  [{}] - {}".format(i, err))
        sys.exit(-1)
    return mtestclass


def header(text):
    cols=70
    border=4
    print('-'*cols)
    print(text.center(cols))
    print('-'*cols)



def default_solution_name():
    test_fname = os.path.basename(__file__)
    test_fname = os.path.splitext(test_fname)[0]
    if test_fname[:5] == 'test_' and test_fname[-7:] == "_secret":
        # secret test?
        return test_fname[5:-7]
    elif test_fname[:5] == 'test_':
        # public test?
        return test_fname[5:]

    # File non presente:
    print(f"ERRORE: nome del file di test non è valido",file=sys.stderr)
    print(f"",file=sys.stderr)
    print(f"Un file di test deve chiamarsi test_XXXX.py o test_XXXX_secret.py",
          file=sys.stderr)
    sys.exit(-1)


def check_file_presence(nome_file):

    sol_name=nome_file+".py"
    test_name = os.path.basename(__file__)

    if os.path.isfile(sol_name): return

    # File non presente:
    print(f"ERRORE: Impossibile trovare il programma {sol_name}",file=sys.stderr)
    print(f"",file=sys.stderr)
    print(f"SUGGERIMENTI:",file=sys.stderr)
    print(f"    - Il nome del tuo file è *esattamente* {sol_name}?",file=sys.stderr)
    print(f"    - {sol_name} è nella stessa cartella di {test_name}?",file=sys.stderr)
    sys.exit(-1)

def run_all_tests(tests,fvalue):
    test_class = build_test_class(tests,fvalue)

    # Testa le soluzioni degli studenti e segnala eventuali errori
    suite = unittest.TestSuite()
    suite.addTests( unittest.TestLoader().loadTestsFromTestCase( test_class ) )
    runner = unittest.TextTestRunner()
    runner.run(suite)

# ------------------------- INIZIA A SCRIVERE QUI --------------------------

# Struttura dati 'Testcase' per i casi di test
#
#   name    - nome del test
#   fname   - nome della funzione da testare (opzionale, vedi sotto)
#   input   - tupla contenente gli argomenti della funzione per il test
#   result  - valore atteso
#   error   - errore atteso
#   inplace - modifica attesa dell'input
#   explanation - spiegazione dell'errore (opzionale)
#
#   REQUISITI:
#       - 'name' e 'input' sono campi necessari;
#       - 'fname' è necessario se non viene fornito un default in 'populate_test_class'
#       - deve essere presente esattamente uno 'result', 'error', e 'inplace';
#       - non ci possono essere due test con nomi uguali (a meno di spazi).

# ------ START TEST SECTION ------

casi_di_test =[
    Testcase(name="liste vuote", input=([],[]), result=[]),
    
    Testcase(name="singleton 1", input=([5],[5]), result=[5]),
    Testcase(name="singleton 2", input=([3],[5]), result=[]),
    
    Testcase(name="no intersezione", input=([7,1],[8,12]), result=[]),
    Testcase(name="esempio 1", input=([8, 6, 4, 5, 2],[2, 5, 6, 4, 8]), result=[2, 4, 5, 6, 8]),
    Testcase(name="esempio 2", input=([8, 1, 4, 5, 2],[2, 5, 6, 4, 18]), result=[2,4,5]),
    Testcase(name="esempio 3", input=([2,4,3,1],[4,1,5]), result=[1,4])
]



# ------ END   TEST SECTION ------



if __name__ == '__main__':

    nome_funzione = default_solution_name()
    nome_file     = default_solution_name()

    # Controlla l'esistenza del file
    check_file_presence(nome_file)

    # Importa le soluzioni degli studenti e segnala eventuali problemi
    load_solution_file(nome_file, nome_funzione)

    # Trova la funzione e la testa
    funzione = globals()[nome_funzione]

    header(f"TEST per {nome_file}.py")
    print()
    print("La riga che rappresenta l'esito dei test contiene:")
    print("    - un punto . per ogni risultato corretto")
    print("    - un carattere F per ogni risultato sbagliato")
    print("    - un carattere E per ogni test impossible da eseguire")
    print()

    if 'casi_di_test' in globals():
        tests = casi_di_test
    elif 'casi_di_test_sec' in globals():
        tests = casi_di_test_sec
    else:
        tests = []

    # Esegue i test
    run_all_tests(tests, funzione)

