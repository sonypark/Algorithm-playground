import sys
n = int(sys.stdin.readline())
s = map(int,sys.stdin.readline().split())
count = 0
total = 0

for i in s:
    if i == 1:
        total += 1 + count
        count += 1
    else:
        count = 0
print(total)