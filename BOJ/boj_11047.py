import sys
n,m = map(int, input().split())
limit_length = 2*len(str(m))
if 2*len(str(m)) >n:
    limit_length = n
x = [int(sys.stdin.readline().rstrip()) for _ in range(limit_length)]
count = 0
while len(x) !=0:
    c = x.pop()
    mod = m // c
    if mod == 0:
        continue
    m -= c*mod
    count += mod
print(count)


## 다른 사람 풀이
import sys
n,k = map(int,sys.stdin.readline().split())
m=[]
for i in range(n):
    m.append(int(sys.stdin.readline()))
count=0
for i in reversed(m):
    count += k // i
    k %= i
print(count)



#
# import sys
# n,m = map(int, input().split())
# limit_length = 2*len(str(m))
# if 2*len(str(m)) >n:
#     limit_length = n
# x = [int(sys.stdin.readline().rstrip()) for _ in range(limit_length)]
# count = 0
# for i in range(len(x)-1,-1,-1):
#     print(m)
#     while m // x[i] !=0:
#         m -= x[i]
#         count +=1
# print(count)

