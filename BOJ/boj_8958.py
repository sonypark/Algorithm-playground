'''
OX퀴즈
'''
import sys
n = int(input())

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    answer = []
    a = 0
    for i in s:
        if(i == 'O'):
            a += 1
            answer.append(a)
        if(i == 'X'):
            a = 0
    print(sum(answer))
