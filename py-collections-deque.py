#https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
from collections import deque


s = deque()
rep_command = int(input())

#Excec takes a str input and passes the information in the form of a command
for _ in range(rep_command):
    cmd = input().split() 
    try:
        exec(f"s.{cmd[0]}({cmd[1]})")
    except:
        exec(f"s.{cmd[0]}()") 

print(' '.join(map(str, list(s))))
