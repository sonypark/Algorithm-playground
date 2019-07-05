import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

a = [[] for _ in range(N+1)]

for i in range(M):
    v1,v2 = map(int, sys.stdin.readline().split())
    a[v1].append(v2)
    a[v2].append(v1)

visited = [False] * (N+1)


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    visit_route = []
    while q:
        d = q.popleft()
        visit_route.append(d)

        for i in a[d]:
            if visited[i] is False:
                visited[i] = True
                q.append(i)
    return visit_route


CC = []
for v in range(1, N+1):
    if visited[v] is False:
        CC.append(bfs(v))
print(len(CC))