#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""*********************************************************************
  Informatica 2019/2020
  
  Casi di test per: {0}
  Funzioni:
{1}
  

RACCOMANDAZIONI:  

anche se non capite tutte le informazioni prodotte da questo
programma, leggete quelle che capite perché vi possono aiutare nello
svolgimento degli esercizi.
"""
ex_name      ='labMio'
ex_functions =['somma_lista'] 


#---------------------------------------------------
import importlib
import unittest
import sys
import os

# Stampa un'intestazione che descrive l'esercizio
lista_delle_funzioni="\n".join("  -"+f for f in ex_functions)
print(__doc__.format(ex_name,lista_delle_funzioni))


errori_preliminari=False   # il file ha la giusta struttura?

# Importa le soluzioni degli esercizi
print("CONTROLLO PRELIMINARE DEL FILE {0}.py:".format(ex_name))

lab=None
try:
    lab=importlib.__import__(ex_name)
except Exception:
    msg="""
    Problema a importare il file {0}.py:
    -- il file potrebbe non essere presente in questa cartella,
    -- oppure potrebbe contenere errori che lo rendono non eseguibile.
    
    Provate ad eseguire il comando 'python3 {0}.py' da terminale per
    avere più informazioni. """.format(ex_name)
    print(msg)
    errori_preliminari = True
else:
    #Carica nel namespace le funzioni definite
    f_objects={}
    for f_name in ex_functions:
        try:
            f_object = lab.__dict__[f_name]
            f_objects[f_name] = f_object
        except KeyError:
            msg="    Esercizio mancante: la funzione {1} non è presente nel file {0}.py".format(ex_name,f_name)
            print(msg)
            errori_preliminari = True
        else:
            msg="    Esercizio trovato: la funzione {1} è presente in file {0}.py".format(ex_name,f_name)
            print(msg)
        globals().update(f_objects)


goodhelptext="""
INIZIO DEI TEST AUTOMATICI:

Il file delle soluzioni sembra avere la struttura corretta,
quindi i test avranno luogo.

La prima riga subito dopo la cornice di asterischi contiene:
- un punto . per ogni test riuscito
- una carattere F per ogni test fallito
- un carattere E per ogni test che non è stato possiblie eseguire
**********************************************************************
*******                     ESITO DEI TEST                     *******
**********************************************************************
"""
badhelptext="""
ANNULLAMENTO DEI TEST AUTOMATICI:

Le verifiche automatiche non possono partire perché il file non
esiste, non è eseguibile, oppure non contiene tutte le soluzioni 
degli esercizi. 

Sistemate il file delle soluzioni e rieseguite i test.
**********************************************************************
"""
if errori_preliminari:
    print(badhelptext)
    sys.exit(-1)
else:
    print(goodhelptext)

from pprint import pformat


class TestLabMioSommaLista(unittest.TestCase):

    def errormsg(self,lista,expected,result):
        if len(lista)==0:
            messaggio = """

MOTIVO DEL FALLIMENTO:
    La somma degli elementi della lista vuota è {1}, e invece il programma 
    restituisce {2}"""
        else:
            messaggio = """

MOTIVO DEL FALLIMENTO:
    Le vocali nella stringa
    '{0}'
    sono {1}, e invece il programma restituisce {2}"""
        messaggio = messaggio.format(lista,expected,result)
        return messaggio
    
    def test_lista_vuota(self):
        lista=[]
        expected=0
        result=somma_lista(lista)
        msg=self.errormsg(lista,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_lista_singleton(self):
        lista=[5]
        expected=5
        result=somma_lista(lista)
        msg=self.errormsg(lista,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista_lunga(self):
        lista=[7, 1, 3, 4, -3]
        expected=12
        result=somma_lista(lista)
        msg=self.errormsg(lista,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_non_lista(self):
        lista=1000
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione somma_lista su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo liste come argomento."""
        messaggio = messaggio.format(repr(lista))
        with self.assertRaises(TypeError,msg=messaggio):
            somma_lista(lista)

    def test_lista_non_numerica(self):
        lista=[3, "pippo", 5]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione somma_lista su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo liste contenenti numeri come argomento."""
        messaggio = messaggio.format(repr(lista))
        with self.assertRaises(TypeError,msg=messaggio):
            somma_lista(lista)

        

        
if __name__ == '__main__':
    unittest.main()
                              

    
