import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
sum = 0
for a,b in zip(sorted(a),sorted(b,reverse=True)):
    sum += a*b
print(sum)