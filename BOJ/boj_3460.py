import sys
n = int(input())

for i in range(n):
    a = int(sys.stdin.readline())
    b = []
    while a != 1:
        b.append(a % 2)
        a = a // 2
    b.append(a)
    for k in range(len(b)):
        if b[k] ==1:
            print(k, end=" ")