#Parts of the following code were assisted by ChatGPT

from itertools import combinations

lista = input().split()
text, times = str(lista[0]),int(lista[1])+1

almacen_1 = []
almacen_2 = []

for i in range(1, times):
    almacen_2 = list(combinations(sorted(text),i))
    almacen_1 = almacen_1+almacen_2

for elemento in almacen_1:
    cadena = ''.join(str(i) for i in elemento)
    print(cadena)
