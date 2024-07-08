#Code created with assistance of ChatGPT

repeat = int(input())

for i in range(repeat):
    ignore_me = input()
    subset_a = set((input().split()))
    ignore_me2 = input()
    subset_b = set((input().split()))
    resultado = all(elemento in subset_b for elemento in subset_a)
    print(resultado)
