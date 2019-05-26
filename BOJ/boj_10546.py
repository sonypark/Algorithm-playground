import sys
## 시간 초과
n = int(input())

p = []
for _ in range(n):
    a = sys.stdin.readline()
    p.append(a)

c = []
while True:
    b = sys.stdin.readline()
    if b in p:
        p.remove(b)
    if len(p) ==1:
        print(p[0])
        break


## 내 풀이 - collections.Counter 이용
import sys
import collections

n = int(input())

p = []
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    p.append(a)

c = []
while len(c) != len(p)-1:
    b = sys.stdin.readline().rstrip()
    c.append(b)

count_p = collections.Counter(p)
count_c = collections.Counter(c)
print(list((count_p - count_c).keys())[0])



## 다른 사람 풀이
import sys
input = sys.stdin.readline
N = int(input())
mara = dict()

for i in range(2*N-1):
    name = input().strip()
    # print(name in mara)
    try:
        del mara[name]
    except:
        mara[name] = 1
    print(mara)

print("".join(list(mara.keys())))