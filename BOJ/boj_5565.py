import sys
tp = int(sys.stdin.readline())

price =0
for i in range(9):
    a = int(sys.stdin.readline())
    price +=a
print(tp - price)

## 다른 사람 풀이
Total = int(input())
for _ in range(9):
    Total -= int(input())
print(Total)

## 다른 사람 풀이
a=[int(input())for _ in range(10)]
print(a[0]-sum(a[1:]))

