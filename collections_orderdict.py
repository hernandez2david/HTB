#Code generated with assistance of ChatGPT
#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

n = int(input())

# Initialize an empty dictionary to store items and costs
items_dict = {}

# Parse input and construct the dictionary
for _ in range(n):
    #Doble asignacion, rsplit con maxsplit hace un máximo de 1 separacion hacia la derecha
    item, cost = input().rsplit(maxsplit=1)
    
    #tenemos item=BANANA FRIES y cost=12. items_dict.get(item) va a iniciarlizar el valor de item en 0 en caso que item no exista.. En la misa línea, le sumará el costo una vez creado o si lo encuentra 
    items_dict[item] = items_dict.get(item, 0) + int(cost)

# Print the constructed dictionary
print("-")
for i in items_dict:
    print(i+" "+str(items_dict[i]))
