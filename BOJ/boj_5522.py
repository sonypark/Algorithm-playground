import sys
s=0
for _ in range(5):
    a = int(sys.stdin.readline())
    s += a
print(s)

## 다른 사람 풀이
print(sum([int(input()) for x in range(5)]))
