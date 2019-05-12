import sys
import functools
n = int(sys.stdin.readline())
'''
birthday = []
for i in range(n):
    name, d,m,y = sys.stdin.readline().split()
    birthday.append([name, int(d), int(m), int(y)])


def compareBirthDay(a, b):
    if a[3] == b[3]:
        if a[2] == b[2]:
            return a[1] - b[1]
        return a[2] - b[2]
    return a[3] - b[3]

birthday.sort(key=functools.cmp_to_key(compareBirthDay))
print(birthday[-1][0])
print(birthday[0][0])


# 다른 사람 풀이
def finde(x):
    return x[0],x[1],x[2]

test = int(input())
list = []
for i in range(test):
    a = input().split()
    list.append([int(a[3]), int(a[2]), int(a[1]), a[0]])
list = sorted(list, key = finde)
print(list[len(list)-1][3])
print(list[0][3])
'''

## 다른 사람의 풀이를 보고 적용한 내 풀이
birthday = []
for i in range(n):
    name, d,m,y = sys.stdin.readline().split()
    birthday.append([name, int(d), int(m), int(y)])

def compareBirthDay(x):
    return x[3],x[2],x[1]

birthday.sort(key=compareBirthDay)
print(birthday)
print(birthday[-1][0])
print(birthday[0][0])