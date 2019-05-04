import sys
n = int(input())


for i in range(n):
    a,b,c = map(int, sys.stdin.readline().split())
    m = b-c
    if m - a > 0:
        print('advertise')
    elif m - a == 0:
        print('does not matter')
    else:
        print('do not advertise')
