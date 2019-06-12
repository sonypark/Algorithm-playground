import sys

a, b = map(int, sys.stdin.readline().split())


def primeNum(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = int(n ** 0.5) + 1
    for i in range(3, m, 2):
        if n % i == 0:
            return False
    return True


for j in range(a, b + 1):
    if (primeNum(j)):
        print(j)


# Python program to print all primes smaller than or equal to n using Sieve of Eratosthenes

# def SieveOfEratosthenes(n):
#     # Create a boolean array "prime[0..n]" and initialize
#     # all entries it as true. A value in prime[i] will
#     # finally be false if i is Not a prime, else true.
#     prime = [True for i in range(n + 1)]
#     p = 2
#     while (p * p <= n):
#
#         # If prime[p] is not changed, then it is a prime
#         if (prime[p] == True):
#
#             # Update all multiples of p
#             for i in range(p * 2, n + 1, p):
#                 prime[i] = False
#         p += 1
#
#     # Print all prime numbers
#     for p in range(2, n):
#         if prime[p]:
#             print(p)
#
#
# # driver program
# if __name__ == '__main__':
#     n = 30
#     print("Following are the prime numbers smaller than or equal to")
#     SieveOfEratosthenes(n)


import sys

def sieve(start, end):
    if end < 2:
        return []
    sieve_list = [False, False] + [True] * (end-1)
    for i in range(2, int(end**0.5)+1):
        if sieve_list[i]:
            sieve_list[i*2::i] = [False] * ((end-i)//i)
    return [i for i, v in enumerate(sieve_list) if v and i >= start]


M, N = map(int, sys.stdin.readline().split())

prime_num_list = sieve(M, N)

for p in prime_num_list:
    print(p)
