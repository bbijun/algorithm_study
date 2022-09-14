import sys
from collections import deque
input = sys.stdin.readline
result = 0
dx = [-1,0,0,1]
dy = [0,-1,1,0]
n = int(input())
maze = []
x = y = 0
weight = 2
count = 0
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        x = _
        y = tmp.index(9)
    maze.append(tmp)
q = deque()
q.append((x,y,0))
maze[x][y] = 0
visited[x][y] = True
while q:
    x,y,move = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= len(maze) or nx <= -1 or ny >= len(maze) or ny <= -1 or maze[nx][ny] > weight:
            continue
        if 0 < maze[nx][ny] < weight:
            q.clear()
            count += 1
            if count == weight:
                weight += 1
                count = 0
            maze[nx][ny] = 0
            result += move + 1
            q.append((nx, ny, 0))
            maze[nx][ny] = 0
            visited = [[False] * n for _ in range(n)]
            visited[nx][ny] = True
            #print("(%d, %d), r= %d, w = %d" %(nx+1, ny+1, result, weight))
            break

        elif maze[nx][ny] == weight or maze[nx][ny] == 0:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, move + 1))
            else:
                continue
        else:
            continue
print(result)

