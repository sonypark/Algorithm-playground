import sys
a,b = map(int, sys.stdin.readline().split())
a, b = max(a,b), min(a,b)

# 유클리드 호제법
def gcd(a,b):
    remainder = a % b
    while remainder !=0:
        a = b
        b = remainder
        remainder = a % b
    return b
GCD = gcd(a,b)
print(GCD)
print(int(a*b/GCD))


## 다른 사람 풀이
n,m=map(int,input().split())
def gcd(a,b):return gcd(b, a%b) if b else a
print(gcd(n, m));print(n*m//gcd(n,m))