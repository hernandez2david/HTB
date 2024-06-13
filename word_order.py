#code created with assistance of ChatGPT 
#https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=false

n = int(input())  # Lee el número de palabras

# Crea un diccionario vacío para almacenar cada palabra y su frecuencia
word_freq = {}

# Itera a través de las palabras y cuenta su frecuencia
for i in range(n):
    word = input().strip()  # Lee la i-ésima palabra y elimina los espacios en blanco iniciales y finales
    word_freq[word] = word_freq.get(word, 0) + 1  # Incrementa la frecuencia de la palabra por 1

# Imprime el número de palabras distintas
#print(len(word_freq))

print(word_freq)

# Imprime la frecuencia de cada palabra según su aparición en la entrada
for word in word_freq:
    print(word_freq[word], end=' ')
