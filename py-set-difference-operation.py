#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
#py-set-difference-operation
r = int(input())
s = set(input().split())

z = int(input())
n = set(input().split())

print(len(s - n))
