#Parts of the following code were assisted by ChatGPT
#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true

from itertools import combinations_with_replacement

lista = input().split()
text, times = str(lista[0]),int(lista[1])

almacen_1 = []
almacen_2 = []

#Generates the list of combinations and sorts such list in lexicographical order
almacen_2 = list(combinations_with_replacement(sorted(text),times))
almacen_1 = almacen_1+almacen_2

for elemento in almacen_1:
    cadena = ''.join(str(i) for i in elemento)
    print(cadena)
