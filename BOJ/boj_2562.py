import sys

max = 0
idx = 0
for i in range(1,10):
    n = int(sys.stdin.readline())

    if max < n:
        max = n
        idx = i
print(max)
print(idx)


## 다른 사람 풀이
## more Declarative 한 풀이
A = [int(input()) for _ in range(9)]
print(max(A))
print(A.index(max(A))+1)