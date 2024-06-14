#Code generated and documented with assistance of ChatGPT. 
#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

# Lee el tamaño y los elementos del primer conjunto
M = int(input())
#map aplica operaciones multiples veces sobre una lista. En este caso convierte los elementos individuales a int.
a = set(map(int, input().split()))

# Lee el tamaño y los elementos del segundo conjunto
N = int(input())
b = set(map(int, input().split()))

# Calcula la diferencia simétrica entre los dos conjuntos
#La siguiente funcion genera la diferencia simetrica entre los sets de datos. El resultado no esta ordenado, asi que usamos sorted para ordenarlos de menor a mayor
diferencia_simetrica = (a.symmetric_difference(b))


# Imprime los elementos de la diferencia simétrica
print(diferencia_simetrica)
for elemento in diferencia_simetrica:
    print(elemento)
