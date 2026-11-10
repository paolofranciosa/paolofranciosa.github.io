#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019, 2020, 2021, 2023 by Massimo Lauria <massimo.lauria@uniroma1.it>
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

headertext = """
*********************************************************************
  Informatica {anno}

  Test per il programma: {file}.py
  Funzioni:
{functions}


RECOMMENDATIONS:

even if you do not understand all the information produced by this
program, read the ones you do understand because they can help you in the
performance of the exercises."""

goodhelptext = """
START OF AUTOMATED TESTING:

The solutions file seems to have the correct structure,
so the tests will take place.

The line representing the outcome of the tests contains:
- a dot . for each successful test
- an F character for each failed test
- an E character for each test that could not be run
**********************************************************************
*******                  RESULTS OF THE TESTS                  *******
**********************************************************************
"""

badhelptext = """
CANCELLATION OF AUTOMATIC TESTS:

Automatic tests cannot start because the file does not
exists, is not executable, or does not contain all the solutions
of the exercises.

Fix the solutions file and re-run the tests.
**********************************************************************
"""


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
    if not isinstance(filename_woext, str):
        print(
            "ERROR IN THE TEST FILE: the name of the solutions file is invalid."
        )
        sys.exit(-1)

    if isinstance(functions, str):
        functions = [functions]

    for s in functions:
        if not isinstance(s, str):
            print(
                "ERROR IN THE TEST FILE: the name of the solutions file is invalid."
            )
            sys.exit(-1)

    # Stampa un'intestazione che descrive l'esercizio
    lista_delle_funzioni = "\n".join("  - " + f for f in functions)
    print(
        headertext.format(anno='2020/2021',
                          file=filename_woext,
                          functions=lista_delle_funzioni))

    errori_preliminari = False  # il file ha la giusta struttura?

    # Importa le soluzioni degli esercizi
    print("PRELIMINARY FILE CHECK {0}.py:".format(filename_woext))

    lab = None
    try:
        lab = importlib.__import__(filename_woext)
    except Exception:
        msg = """
        Problem importing the file {0}.py:
        -- the file may not be present in this folder,
        -- or it may contain errors that make it not executable.

        Try running the command 'python3 {0}.py' from a terminal to
        get more information. """.format(filename_woext)
        print(msg)
        errori_preliminari = True
    else:
        # Carica nel namespace le funzioni definite
        f_objects = {}
        for f_name in functions:
            try:
                f_object = lab.__dict__[f_name]
                f_objects[f_name] = f_object
            except KeyError:
                msg = "    Missing exercise: function {1} is not present in file {0}.py".format(
                    filename_woext, f_name)
                print(msg)
                errori_preliminari = True
            else:
                msg = "    Exercise found: function {1} is present in file {0}.py".format(
                    filename_woext, f_name)
                print(msg)

            globals().update(f_objects)

    if errori_preliminari:
        print(badhelptext)
        sys.exit(-1)
    else:
        print(goodhelptext)


def error_msg(testcase, computed=TcUndef, backup=TcUndef):
    messaggio1 = """

WHY the '{0}' test for function '{1}' failed :""".format(
        testcase.name, testcase.fname)

    if testcase.result is not TcUndef:
        messaggio2 = """
    The result that was calculated with the parameters {0} is {2}, whereas instead
    it should be {1}""".format(repr(testcase.input), testcase.result,
                                  computed)

    elif testcase.inplace is not TcUndef:
        messaggio2 = """
    The function was supposed to change the input {0} to {1}, 
    instead it produced {2}""".format(repr(backup), repr(testcase.inplace),
                                     repr(testcase.input))

    elif testcase.error is not TcUndef:
        messaggio2 = """
    The function on parameters {} should raise '{}'""".format(
            repr(testcase.input), str(testcase.error))

    else:
        raise ValueError(
            "Test {} contains neither 'error' nor 'result' nor 'inplace'".
            format(testcase.name))

    if testcase.explanation is TcUndef:
        messaggio3 = ''
    else:
        messaggio3 = ", because {}".format(testcase.explanation)

    return messaggio1 + messaggio2 + messaggio3


def generate_test_function(testcase):

    if testcase.fname is TcUndef or testcase.fvalue is TcUndef:
        raise AttributeError("'{}' Does not contain the 'fname' and 'fvalue' fields, which are required.".format(testcase.name))

    if testcase.input is TcUndef:
        raise AttributeError(
            "'{}' does not contain the 'input' field, which is necessary.".format(
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
        raise AttributeError("'{}' must have exactly one field between "
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
        raise RuntimeError("'{}' we shouldn't have gotten here!!!".format(
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
        print("ERROR IN TEST CASES:")
        for i, err in errori_nei_test:
            print("  [{}] - {}".format(i, err))
        sys.exit(-1)
    return mtestclass


def default_solution_name():
    test_fname = os.path.basename(__file__)
    test_fname = os.path.splitext(test_fname)[0]
    if test_fname[:5] == 'test_' and test_fname[-7:] == "_secret":
        # secret test?
        return test_fname[5:-7]
    elif test_fname[:5] == 'test_':
        # public test?
        return test_fname[5:]
    else:
        raise ValueError(
            "Non è possibile determinare il nome dell'esercizio dal nome del file di test."
        )

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

casi_di_test = [
    # Write test cases there according to format
    #
    # Testcase(field1=value1, field2=value2, ...)
    #
    # The most common test case is something like
    #
    # Testcase(name='Sorted input', input=([1,2,3,4],),   result=True)
    # Testcase(name='Shuffled input', input=([4,2,1,3],), result=True)
    # Testcase(name='Empty list', input=([],), result=False)
    #
    # All test names in a single file must be different.
    Testcase(name="argument 2", input=(2,), result={1: 1}),
    Testcase(name="argument 3", input=(3,), result={1: 1, 2: 4}),
    Testcase(name="argument 4", input=(4,), result={1: 1, 2: 4, 3: 9}),
]


# ------ END   TEST SECTION ------



if __name__ == '__main__':

    nome_funzione = default_solution_name()
    nome_file     = default_solution_name()

    # Importa le soluzioni degli studenti e segnala eventuali problemi
    load_solution_file(nome_file, nome_funzione)

    # Trova la funzione e la testa
    funzione = globals()[nome_funzione]

    if 'casi_di_test' in globals():
        tests = casi_di_test
    elif 'casi_di_test_sec' in globals():
        tests = casi_di_test_sec
    else:
        tests = []

    run_all_tests(tests, funzione)

