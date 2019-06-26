import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

# 간선의 개수 만큼 for 문을 돌며 연결한다.
# 인접 리스트를 만든다.
for _ in range(M):
    x,y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# 문제 조건 상 정점이 여러개인 경우 번호가 작은 것을 먼저 순회하므로 정렬해준다.
for i in range(1, N+1):
    graph[i].sort()

def dfs(now, visited=None, visit_route=[]):
    if visited is None:
        visited = [False] * (N+1)

    # 현재 노드 방문 체크
    visited[now] = True
    # 현재 노드 방문 루트에 추가
    visit_route.append(now)
    # 현재 노드의 자식 노드들을 하나씩 꺼냄
    for i in graph[now]:
        # 해당 자식 노드에 방문한 적이 없는 경우 들어가 탐색
        if visited[i] is False:
            dfs(i, visited, visit_route)

    # 최종 방문 루트를 출력
    return visit_route


def bfs(v):
    visited = [False] * (N+1)
    visit_route =[]
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        now = q.popleft()
        visit_route.append(now)

        for i in graph[now]:
            if visited[i] is False:
                visited[i] = True
                q.append(i)

    return visit_route


print(' '.join(map(str, dfs(V))))
print(' '.join(map(str, bfs(V))))




## 인접 행렬을 이용한 풀이


# 인접 행렬 생성
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]


# 연결된 노드들은 1로 표시한다.
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1


def dfs(now, visited=None, visit_route=[]):
    if visited is None:
        visited = [False] * (N+1)
    visited[now] = True
    visit_route.append(now)

    # 현재 노드와 연결되어 있고 아직 방문하지 않은 자식 노드 탐색
    for i in range(1, N+1):
        if graph[now][i] == 1 and visited[i] is False:
            dfs(i, visited, visit_route)
    return visit_route

def bfs(v):
    visited = [False] * (N+1)
    visit_route = []
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        visit_route.append(now)
        # 현재 노드와 연결되어 있고 아직 방문하지 않은 자식 노드 탐색
        for i in range(1, N+1):
            if graph[now][i] == 1 and visited[i] is False:
                visited[i] = True
                q.append(i)
    return visit_route


print(dfs(V))
print()
print(bfs(V))
