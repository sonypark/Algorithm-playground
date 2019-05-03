import sys

def biggerNum(a,b):
    if (a > b):
        print('Yes')
    else:
        print('No')

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    biggerNum(a,b)
