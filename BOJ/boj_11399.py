import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))

s = 0
for i in range(len(a)):
    s += sum(a[:1+i])
print(s)


## 다른 사람 풀이
input()
a=sorted(map(int,input().split()))
p = [a[i]*(len(a)-i) for i in range(len(a))]

