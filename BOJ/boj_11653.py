import sys
n = int(sys.stdin.readline())

# 1
def getprime(n):
    for x in range(2, n + 1):
        count = 0    # 인수가 곱해진 횟수
        while n % x == 0:
            count += 1
            n /= x
        if count != 0:
            for i in range(count):
                print ("%d" % x)
# getprime(n)


# 2
for i in range(2, int(n**0.5)+1):
    while n % i == 0:
        n = n // i
        print(i)
if n > 1:
    print(n)



# 어디가 틀린걸까..?
primeNum = []
answer = []

def prime_number(n):
    if n == 1:  return False
    if n == 2:  return True
    if n == 3:  return True
    if(n%2==0): return False

    m = int(n ** 0.5) + 1
    for i in range(3, m,2):
        if n % i == 0: return False
    return True

for j in range(n):
    if(prime_number(j)):
        while n % j ==0:
            answer.append(j)
            n = n // j
        if n == 1: break
        if (prime_number(n)):
            answer.append(n)
            break

for a in answer:
    # print(a)
    pass