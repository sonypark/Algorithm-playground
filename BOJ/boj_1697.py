import sys
from collections import deque

q = deque()
dist = dict()

N, K = map(int, sys.stdin.readline().split())


def bfs():
    q.append(N)
    dist[N] = 0

    while q:
        x = q.popleft()
        if x == K:
            return dist[x]
        for nx in (x-1), (x+1), (2*x):
            if nx < 0 or nx > 100000: continue
            if dist.get(nx) is None:
                dist[nx] = dist[x]+1
                q.append(nx)

print(bfs())