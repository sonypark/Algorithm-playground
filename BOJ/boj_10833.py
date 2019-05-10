import sys
n = int(sys.stdin.readline())
apple_remainder = 0
for _ in range(n):
    a,b= map(int, sys.stdin.readline().split())
    apple_remainder += b % a
print(apple_remainder)