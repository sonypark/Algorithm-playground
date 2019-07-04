from  collections import deque
n = int(input())

adj = [[] for _ in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        if a[j]:
            adj[i].append(j)

def bfs(v, d):
    q = deque()
    q.append(v)
    visited = [False] * n
    state = False

    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            for e in adj[v]:
                if e == d:
                    print(1, end=" ")
                    state = True
                    break
                if not(visited[e]):
                    q.append(e)
            if state:
                break
    else:
        print(0, end=" ")


for i in range(n):
    for j in range(n):
        bfs(i, j)
    print()



## 다른 사람 풀이
import sys
input = sys.stdin.readline


def dfs(e, f, status):
    if not status:
        visited[e] = 1
        adj[f][e] = 1
    for elem in pt[e]:
        if not visited[elem]:
            dfs(elem, f, 0)


n = int(input())
arr = []
adj = [[0]*n for _ in range(n)]
pt = {}
for i in range(n):
    arr.append(list(map(int, input().split())))
    pt[i] = []
    for j in range(n):
        if arr[i][j] == 1:
            pt[i].append(j)

for i in range(n):
    visited = [0] * n
    dfs(i, i, 1)

for elem in adj:
    print(*elem)


## 다른 사람 풀이 - DFS 재귀
n = int(input())

adj_list = [[] for i in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    adj_list[i] = [idx for idx, value in enumerate(temp) if value == 1]


def dfs(a, visit):

    ## 자신과 인접한 자식 노드를 찾는다.
    for ad in adj_list[a]:
        if visit[ad] == 0:
            visit[ad] = 1
            dfs(ad, visit)


for i in range(n):
    visit = [0] * n
    dfs(i, visit)
    print(*visit)
