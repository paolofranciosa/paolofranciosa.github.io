---
title: Prova di Informatica@DSS {yearstring}
date: {description}
fontsize: 12pt
papersize: a4
numbersections: true
author:
Paolo Franciosa
header-includes: |
    \usepackage{parskip}
    \usepackage{fancyvrb}
    \fvset{fontsize=\small,numbers=none,numbersep=-12pt}
    \RecustomVerbatimEnvironment{verbatim}{Verbatim}{frame=single}
    \DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\},numbers=right,numbersep=-12pt}
---
**Working methods**: The exam text, the test files of the
exercises and a synoptic table on Python syntax can be found in the
`exam` folder on your desk, in the "Statistica-Laboratorio" virtual machine.
The solutions to the exercises must be placed in the same folder
`exam`.  **First compile the file** `student.txt` with the
first name, surname and matriculation information
```
nome: Giacomo
cognome: Leopardi
matricola: 123456789
```

Not completing the `student.txt` file is like not handing in
the assignment. For the exam, you can only have

- your ID or passport;
- beverages and snacks;

and you must leave your bags and backpacks in the corner of the room, with mobile phones
and electronic devices switched off inside.

**The grade is the sum of the points of the exercises**, so it is possible to
get 30 even without completing them all.

**Use of test files**: tests check very
briefly the setting of the solutions and passing the tests does not
at all imply that the solution is correct. Read the text
of the exercises before starting to solve them. To complete each exercise
exercise you must

- write a solution file **with the specified name**;
- have the function **with the specified name** inside;
- place the solution file in the `exam` folder;
- run the `python3 <testfile>` command in that folder

where `<testfile>` should of course be replaced with the name of the
appropriate test file for the exercise you are working on.

There is an independent test file for each exercise, so you can
work on the exercises one at a time with more ease.  The result of
each test is a screen (or several screens) showing

- whether the file with the correct name was found,
- whether the file contains the function with the correct name,
- whether calls to the function with different parameter values end by returning correct results.

For each function written, calls are made with different values
of the parameters. The result of the tests is returned with the character

- `E` if the call cannot be executed,
- `F` if the function does not return the correct result,
- `.` if the function returns the correct result.