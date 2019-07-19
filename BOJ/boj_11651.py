import sys
n = int(input())

a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def cmp(x):
    return x[1], x[0]

a.sort(key=cmp)
for v in a:
    print(*v)