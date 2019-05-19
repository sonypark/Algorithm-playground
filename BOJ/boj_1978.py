import sys
input()

def isPrime(n):
    if n<2:
        return False
    if n ==2:
        return True
    if n%2==0:
        return False

    m = int(n**0.5)+1
    for i in range(3,m,2):
        if n % i==0:
            return False
    return True

count = 0
for n in map(int, sys.stdin.readline().split()):
    if isPrime(n):
        count +=1
print(count)
