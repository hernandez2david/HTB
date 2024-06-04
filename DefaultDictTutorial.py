from collections import defaultdict

#Step 1: find a way to manage the input and create the default dictionary assigning the correct values

sizes = input()
sizes = sizes.split()
#converts all the elements in a list into int 
sizes = [eval(i) for i in sizes]

subsets = defaultdict(list)

#Returns the index of a given list in a String format. Prints -1 if the index is not found.
def giving_index(lista, evaluate):
    result = []
    for i,j in enumerate(lista):
        if j == evaluate:
            result.append((i+1))
    result_string = ' '.join(map(str,result))
    if result_string=="":
        result_string="-1"
    return result_string

for i in range(sizes[0]+sizes[1]):
    if i<sizes[0]:
        value = input()
        subsets["a"].append(value)
    if i>=sizes[0]:
        value = input()
        subsets["b"].append(value)

#Uses the elements in subset b and compares each element to get the index. 
for i in subsets["b"]:
    print(giving_index(subsets["a"],i))
