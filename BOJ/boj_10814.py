import sys
n = int(input())

def cmp(x):
    return int(x[1][0]), x[0]

a = [sys.stdin.readline().split() for i in range(n)]
b = list(enumerate(a))
b.sort(key=cmp)

for j in b:
    print(*j[1])



## 다른 사람 풀이
from sys import stdin


def sol():
    N = int(input())
    members = [[] for _ in range(201)]
    for i in range(N):
        age, name = stdin.readline().rstrip().split()
        members[int(age)].append(age + " " + name)
    for member in members:
        for e in member:
            print(e)


if __name__ == "__main__":
    sol()