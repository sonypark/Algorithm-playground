import sys
n = int(sys.stdin.readline())

for _ in range(n):
    c = int(sys.stdin.readline())
    op_num = int(sys.stdin.readline())
    for j in range(op_num):
        a,b = map(int, sys.stdin.readline().split())
        c += a*b
    print(c)

