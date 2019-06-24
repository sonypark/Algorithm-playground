import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

shortest_route = [[0] * M for _ in range(N)]
maze = []
for _ in range(N):
    tmp = list(map(int, list(sys.stdin.readline().rstrip())))
    maze.append(tmp)


def bfs():
    q = deque()
    q.append((0,0))
    shortest_route[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return shortest_route[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if shortest_route[nx][ny] > 0 or maze[nx][ny] == 0: continue

            shortest_route[nx][ny] = shortest_route[x][y] + 1
            q.append((nx, ny))

print(bfs())


