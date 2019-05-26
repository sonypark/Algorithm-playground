import sys
n = int(sys.stdin.readline())

def fibo(n):
    bottom_up = [None]*(n+2)
    if n ==0 : return 0
    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3,n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    print(bottom_up)
    return bottom_up[n]
print(fibo(n))

## 다른 사람 풀이
n = int(input())
a = 0
b = 1
for i in range(n):
    a, b = b + a, a
print(a)