---
title: Programming classwork@DSS {yearstring}
date: {description}
fontsize: 12pt
papersize: a4
numbersections: true
author:
- Paolo Franciosa (credits to prof. Massimo Lauria)
header-includes: |
    \usepackage{parskip}
    \usepackage{fancyvrb}
    \fvset{fontsize=\small,numbers=none,numbersep=-12pt}
    \RecustomVerbatimEnvironment{verbatim}{Verbatim}{frame=single}
    \DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\},numbers=right,numbersep=-12pt}
---

The purpose of the lab is to practice and measure one's
preparation: the exercises are not too difficult, if you have followed
the lectures. However, no score is put on them.

**Working mode**: students should work independently or in
small groups, without disturbing colleagues. Group work is
fruitful only if everyone participates and if everyone writes their own
solution for all exercises.

The teacher will try as much as possible not to occupy the time of the
laboratory to introduce new material, although sometimes this will be
necessary. The lecturer is available to help students, who
can start working even before the lecturer arrives in the classroom,
if they wish.

**Recommendations**: Read the text of the exercises carefully before
ask for clarification. In any case, I will be in the classroom with you.

**Using test files**: To help you complete this exercise
you have test programs available to test your
solution. These are similar to those you will have on the exam,
so I recommend that you learn how to use them. To complete
the exercise you will need to

- write a solution file **with the specified name**;
- have inside the function **with the specified name**;
- place the corresponding test file **in the same folder**;
- run the `python3 <fileditest>` command in that folder;

where `<fileditest>` should obviously be replaced by the name of the
test appropriate for the exercise you are working on. For each
exercise there is an independent test file, so that you can easily work
on the exercises one at a time.

The result of each test is a screen(s) in which
it is shown:

 - whether the file with the correct name was found,
 - whether the file contains the function with the correct name,
 - whether calls to the function with different parameter values
    return correct results.
    
For each function written, calls are made with different values
of the parameters. The outcome of the tests is reported with the character

 - `E` if the call cannot be executed,
 - `F` if the function does not return the correct result,
 - `.` if the function returns the correct result.

