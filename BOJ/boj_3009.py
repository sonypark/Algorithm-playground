'''
<네 번째 점>
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
'''

# 내 풀이
import sys
import collections

x = []
y = []
for _ in range(3):
    a,b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)

counter_x = collections.Counter(x)
counter_y = collections.Counter(y)
xx = [i for i in counter_x if counter_x[i] == 1]
yy = [i for i in counter_y if counter_y[i] == 1]
print(xx[0], yy[0])


# zip 이용
z = []
p = []
for _ in range(3):
    t = tuple(map(int, sys.stdin.readline().split()))
    z.append(t)

zz = list(zip(*z))
for i in zz:
    point = collections.Counter(i)
    p.extend([i for i in point if point[i] ==1])

print(*p)

## 다른 사람 풀이
x = []
y = []
for _ in range(3):
    x1, y1 = map(int, sys.stdin.readline().split())

    if x1 not in x:
        x.append(x1)
    else:
        x.remove(x1)

    if y1 not in y:
        y.append(y1)
    else:
        y.remove(y1)
print(x[0], y[0])

## 다른 사람 풀이
x = []
y = []
p = []
for _ in range(3):
    x1, y1 = map(int, sys.stdin.readline().split())
    x.append(x1)
    y.append(y1)
    x.sort()
    y.sort()

if x[0] == x[1]:
  p.append(x[2])
else:
  p.append(x[0])

if y[0] == y[1]:
  p.append(y[2])
else:
  p.append(y[0])

print(*p)

