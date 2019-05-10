import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    S = []
    D = []
    for i in range(n):
        s,d = sys.stdin.readline().split()
        S.append(s)
        D.append(int(d))
    idx = D.index(max(D))
    print(S[idx])
