#Code generated with assistance of ChatGPT
#https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

repeat = int(input())

my_set = set()

for _ in range(repeat):
    my_set.add(input().strip())

print(len(list(set(my_set))))
