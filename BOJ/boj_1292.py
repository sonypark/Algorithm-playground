import sys
ll = []
a,b = map(int,sys.stdin.readline().split())
for i in range(1, b+1):
    for j in range(1, i+1):
        ll.append(i)
print(sum(ll[a-1:b]))


## 다른 사람 풀이
## 범위가 1000 까지 이므로 배열을 만들어 놓고 계산한다. n+(n+1)/2 에서 n 45 이면 1,035
num_list = []
for i in range(1, 45):
    for j in range(i):
        num_list.append(i)

a, b = map(int, input().split())
sum = 0
for i in range(a-1, b):
    sum += num_list[i]
print(sum)