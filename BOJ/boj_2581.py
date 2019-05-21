a = int(input())
b = int(input())

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

prime_list = []
for n in range(a,b+1):
    if isPrime(n):
        prime_list.append(n)

if len(prime_list) !=0:
    print(sum(prime_list))
    print(min(prime_list))
else: print(-1)