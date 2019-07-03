import sys
from collections import deque

def bfs(i, j, M, N, a):
    q = deque()
    q.append((i, j))
    count = 1

    while q:
        y, x = q.popleft()
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= M or ny >= N: continue

            if a[ny][nx] == 1:
                a[ny][nx] = 0
                count +=1
                q.append((ny, nx))
    return count

def testCase():
    M, N, K = map(int, sys.stdin.readline().split())

    a = [[0] * M for _ in range(N)]
    w = []

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        for i in range(N):
            for j in range(M):
                if i == y and j == x:
                    a[i][j] = 1

    for c in range(N):
        for r in range(M):
            if a[c][r] == 1:
                a[c][r] = 0
                w.append(bfs(c, r, M, N, a))
    print(len(w))


t = int(sys.stdin.readline())

for _ in range(t):
    testCase()


