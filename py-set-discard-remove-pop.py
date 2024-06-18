#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

n = int(input())
s = set(map(int, input().split()))
rep_command = int(input())

#Excec takes a str input and passes the information in the form of a command
for _ in range(rep_command):
    cmd = input().split() 
    try:
        exec(f"s.{cmd[0]}({cmd[1]})")
    except:
        exec(f"s.{cmd[0]}()") 

print(sum(s))

