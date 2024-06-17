#Code created with assistance of ChatGPT
#https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true

#Note: this code had to be submitted as pypy, otherwise the validation for re.error fails and returns True if the regex expression is not valid.

import re

rep = int(input())

entradas = ""
for _ in range(rep):
    entradas = entradas + "\n" + input()

#Delete the initial empty character
entradas = entradas.split("\n")[1:]
print(entradas)

#Validates if the regex expression is correct
for entrada in entradas:
    try:
        re.compile(entrada)
        print(True)
    except re.error:
        print(False)
