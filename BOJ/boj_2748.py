import sys
n = int(sys.stdin.readline())

## 시간 초과
def fibo(n):
    if n >= 3:
        return fibo(n-1) + fibo(n-2)
    else: return 1
print(fibo(n))


## memorization
memo = [None]*(n+1)
def fibo(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n==1 or n==2:
        result = 1
    else:
        result = fibo(n-1,memo) + fibo(n-2,memo)
    memo[n] = result
    return result
print(fibo(n,memo))

## botttom_up
def fibo_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None]*(n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3,n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]
print(fibo_bottom_up(n))


## Jin 풀이
memo = [None] * (n+1)
def fibo(n):
    if n < 2:
        memo[n] = n
        return n

    if memo[n] != None:
        return memo[n]

    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]
print(fibo(n))
