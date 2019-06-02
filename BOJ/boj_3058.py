import sys
n = int(input())
for _ in range(n):
    even = []
    x = list(map(int,sys.stdin.readline().split()))
    for i in x:
        if i % 2 ==0:
         even.append(i)
    print(sum(even), min(even))

