---
title: Esercitazione 8 di Laboratorio Informatica@DSS {yearstring}
date: {description}
author: Paolo Franciosa
fontsize: 12pt
papersize: a4
numbersections: true
header-includes: |
    \usepackage{parskip}
    \usepackage{fancyvrb}
    \fvset{fontsize=\small,numbers=none,numbersep=-12pt}
    \RecustomVerbatimEnvironment{verbatim}{Verbatim}{frame=single}
    \DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\},numbers=right,numbersep=-12pt}
---

Lo scopo del laboratorio è di esercitarsi e misurare la propria
preparazione: gli esercizi non sono troppo difficili, se si sono seguite
le lezioni. Non vi viene comunque messo alcun voto.

**Modalità di lavoro**: gli studenti devono lavorare in autonomia o in
piccoli gruppi, senza disturbare i colleghi. Il lavoro di gruppo è
fruttuoso solo se tutti partecipano e se ognuno scrive una propria
soluzione per tutti gli esercizi.

Il docente cercherà per quanto possibile di non occupare il tempo del
laboratorio per introdurre materiale nuovo, anche se a volte questo sarà
necessario. Il docente è a disposizione per aiutare gli studenti, che
possono iniziare a lavorare anche prima che il docente arrivi in aula,
se lo desiderano

**Raccomandazioni**: leggete bene il testo degli esercizi prima di
chiedere chiarimenti. In ogni caso sarò in aula con voi.

**Uso dei file di test**: per aiutarvi a completare questa esercitazione
avete a disposizione dei programmi di test per testare la vostra
soluzione. Questi sono simili a quelli che avrete in sede di esame,
pertanto vi consiglio di imparate ad usarli. Per portare a termine
l'esercizio è necessario

- scrivere un file di soluzione **col nome specificato**;
- avere dentro la funzione **col nome specificato**;
- porre il file di test corrispondente **nella stessa cartella**;
- eseguire in quella cartella il comando `python3 <fileditest>`

dove `<fileditest>` va  ovviamente sostituito con il nome  del file di
test  appropriato per  l'esercizio su  cui state  lavorando. Per  ogni
esercizio ci sta un file di  test indipendente, così da poter lavorare
sugli esercizi uno alla volta con più agio.

Il risultato di ogni test è una schermata (o più schermate) nella quale
si mostra:

 - se è stato trovato il file con il nome corretto,
 - se il file contiene la funzione con il nome corretto,
 -  se  chiamate  alla  funzione  con  diversi  valori  dei  parametri
   terminano restituendo risultati corretti.

Per ogni funzione scritta vengono eseguite chiamate con diversi valori
dei parametri. L'esito dei test viene riportato con il carattere

 - `E` se la chiamata non può essere eseguita,
 - `F` se la funzione non restituisce il risultato corretto,
 - `.` se la funzione restituisce il risultato corretto.

