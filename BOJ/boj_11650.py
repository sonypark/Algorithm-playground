import sys

t = int(sys.stdin.readline())
c = []

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    c.append((a,b))

def cmp(x):
    return x[0], x[1]

c.sort(key=cmp)

for v in c:
    print(*v)