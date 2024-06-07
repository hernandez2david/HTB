https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

#counts the number of values are received
contador  = int(input())
lista = []

#prints the divisions and handles exceptions
def evaluator(lista):
    try:
        division = int(lista[0])//int(lista[1])
        print(division)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except TypeError as n:
        print(f"Error Code:",n)
    except ValueError as r:
        print(f"Error Code:",r)

#saves the values received into a list that can be indexed
for i in range(contador):
    value = input()
    lista.append(value.split())
#Calls the function evaluator
for e in lista:
    evaluator(e)
