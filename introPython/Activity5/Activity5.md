---
title: Programming classwork@DSS (2022/2023)
date: None
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




\pagebreak
# Set negatives to zero
Write a function `setnegatives(values)` that:

-   expects as an argument a list of numeric values (`int` or `float`)
-   edits the received list, setting all negative items to zero.

The function must return nothing, but it must modify the list passed as an argument. In particular, it is possible to write this function without using the `return` statement. Look in the next example how the function should behave

```{.python}
L = [1.2, -0.4, 5, -2, 12 ]

setnegatives(L)

print(L)
```

```
[1.2, 0, 5, 0, 12]

```




Python code must be saved in file: `setnegatives.py`

Test file: `test_setnegatives.py`

\pagebreak
# Test whether a sequence is bitonic
Write a function `bitonic(L)` that:

-   takes as argument a list `L`;
-   returns `True` if the sequence is  **bitonic**,
    `False` otherwise.

A sequence is considered bitonic if it consists of a **strictly** increasing first part with at least two elements, followed by a **strictly** decreasing part, also consisting of at least two elements. 
For example, the following sequences are bitonic:

-   `2 4 13 34 23`
-   `3 4 1`
-   `27 48 113 134 23 12`

Observe that, as in the examples, the last element of the increasing part is also the first element of the decreasing part.
No bitonic sequence can have less than three elements.  In fact, the list

- `2 4 6 6 3 -2`

is not bitonic because the segment `6 6` is neither strictly increasing nor decreasing.
```{.python}
print(bitonic([2,4,13,34,23]))
print(bitonic([3,4,1]))
print(bitonic([27,48,113,134,23,12]))
print(bitonic([2,4,6,6,3,-2]))
```

```
True
True
True
False

```




Python code must be saved in file: `bitonic.py`

Test file: `test_bitonic.py`

\pagebreak
# List of numbers
Write a function `createlist(a, b)` that:

-   expect as arguments two numbers `a` and
    `b`, with `b` to be a natural number;
-   create and return a list containing the first `b`
    integers starting from `a`. 
    
For example, the instruction `s = crealist1(14.3, 5)` must assign to `s` the list `[15, 16, 17, 18, 19]`.
```{.python}
s = createlist(14.3, 5)
print(s)
s = createlist(14, 7)
print(s)
```

```
[15, 16, 17, 18, 19]
[14, 15, 16, 17, 18, 19, 20]

```




Python code must be saved in file: `createlist.py`

Test file: `test_createlist.py`

\pagebreak
# Intersection
Write a function `intersection(a, b)` that:

-   takes as arguments two lists `a`, `b`;
-   returns a  **sorted** list representing the intersection between the two
    lists, that is, the elements that belong to both list
    `a` and the list `b`. It can be assumed that
    `a` and `b` contain no
    duplicates.
   
To get a sorted copy of a list you can call function `sorted(...)`
    
For example:
```{.python}
L = intersection([2,4,3,1],[4,1,5])
print(L)
```

```
[1, 4]

```




Python code must be saved in file: `intersection.py`

Test file: `test_intersection.py`

\pagebreak
# Local maxima

Write a function `localmaxima(seq)` that:

-   takes as argument a list `seq`;
-   creates and returns a list containing the local maxima in seq.

An element of a sequence is a local maximum if:

- it is not at an extreme of the list;
- it is preceded and followed by elements strictly less than the element
    itself.
   
A list containing fewer than three elements contains no local maximum, so an empty list must be returned in this case.



Python code must be saved in file: `localmaxima.py`

Test file: `test_localmaxima.py`

\pagebreak
# Union
Write a function `union(a, b)` that:

-   takes as arguments two lists `a`, `b`;
-   return a *sorted* list representing the union between the two lists
    `a` and `b`, that is, the elements that belong
    to list `a` and/or list `b`. It can be
    assume that `a` and `b` contain no
    duplicates respectively. However, an element might appear in both
    in `a` and in `b`, and must appear once
    only once in their union.



Python code must be saved in file: `union.py`

Test file: `test_union.py`

