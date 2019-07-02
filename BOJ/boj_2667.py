import sys
from collections import deque

n = int(sys.stdin.readline())
dy = [-1,0,1,0]
dx = [0,-1,0,1]

a = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
apartment = []

def bfs(i,j):
    q = deque()
    q.append((i,j))
    count = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            if a[ny][nx] == 1:
                a[ny][nx] = 0
                count +=1
                q.append((ny, nx))
    return count

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            a[i][j] = 0
            apartment.append(bfs(i,j))

print(len(apartment))
apartment.sort()

for a in apartment:
    print(a)