import sys
n = int(input())
for _ in range(n):
   s = sys.stdin.readline().rstrip()
   print(s[0][0].upper() + s[1:])


