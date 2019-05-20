import sys
max = 0
count = 0
for _ in range(10):
    a,b = map(int,sys.stdin.readline().split())
    count += b - a
    if max < count:
        max = count
print(max)