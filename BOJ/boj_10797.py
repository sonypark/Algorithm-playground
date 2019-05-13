import sys
n = int(sys.stdin.readline())
count = 0
m = map(int, sys.stdin.readline().split())
for i in m:
    if n==i:
        count +=1
print(count)


## 다른 사람 풀이
## count 함수를 잘 이용하자..!
a=input()
b=input()
print(b.count(a))