import sys

n, m = map(int, sys.stdin.readline().split())

d = [[0] * m for _ in range(n)]

for i in range(n):
    a = list(map(int,sys.stdin.readline().rstrip()))
    for j in range(len(a)):
        d[i][j] = a[j]

def biggestSquare(d):
    for i in range(1, n):
        for j in range(1, m):
            if d[i][j] == 1:
                d[i][j] = min(d[i - 1][j], d[i - 1][j - 1], d[i][j - 1]) + 1
            elif d[i][j] == 0: continue

    MAX_COUNT = 0
    for k in range(len(d)):
        M = max(d[k])
        if M > MAX_COUNT:
            MAX_COUNT = M
    return MAX_COUNT **2

print(biggestSquare(d))

