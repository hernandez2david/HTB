#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
#code generated with assistance of ChatGPT

from collections import Counter

tiraleon = input()
lista = input()
lista = lista.split()


contador = Counter(lista)


valor_unico = [key for key, value in contador.items() if value == 1][0]


print(valor_unico)
