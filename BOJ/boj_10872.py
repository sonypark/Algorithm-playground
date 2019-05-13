import sys
n = int(sys.stdin.readline())

def factorial(n):
    if n==0 or n ==1: return 1
    if n ==2: return 2

    bottom_up = [None] * (n+1)
    bottom_up[0] = 1
    bottom_up[1] = 1
    bottom_up[2] = 2

    if bottom_up[n] is not None:
        return bottom_up[n]
    for i in range(3, n+1):
        bottom_up[i] = i * bottom_up[i-1]
    return bottom_up[n]

print(factorial(n))