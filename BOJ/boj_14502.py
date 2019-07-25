import sys
import copy

N,M = map(int, sys.stdin.readline().rstrip().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
virus_list = []
maxVal =0


def getSafeArea(copyMap):
    safe = 0
    for i in range(N):
        for j in range(M):
            if copyMap[i][j] == 0:
                safe +=1
    return safe


# DFS로 바이러스 퍼뜨림
def spreadVirus(x,y, copyMap):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue

        if copyMap[nx][ny] == 0:
            copyMap[nx][ny] = 2
            spreadVirus(nx,ny,copyMap)


def setWalls(start, wall):
    global maxVal

    if wall ==3:
        copyMap = copy.deepcopy(a)

        for i in range(len(virus_list)):
            [virusX, virusY] = virus_list[i]
            spreadVirus(virusX,virusY, copyMap)

        maxVal = max(maxVal, getSafeArea(copyMap))
        return

    for i in range(start, N*M):
        x = int(i / M)
        y = int(i % M)

        if a[x][y] == 0:
            a[x][y] = 1
            setWalls(i+1, wall+1)
            a[x][y] = 0


for i in range(N):
    for j in range(M):
        if a[i][j] == 2:
            virus_list.append([i,j])

setWalls(0,0)
print(maxVal)


