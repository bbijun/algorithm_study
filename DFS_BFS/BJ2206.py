from collections import deque
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
result = 1

#벽을 1이 아닌 -1로 표기
for i in range(n):
    for j in range(m):
        if maze[i][j] == 1:
            maze[i][j] = -1
maze[0][0] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x,y, broken, maze):
    q = deque()
    q.append((x,y,0))
    while q:
        x, y, b = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<= -1 or nx >= n or ny <=-1 or ny >=m:
                continue
            if nx == n-1 and ny == m-1:
                return maze[x][y] +1
            if maze[nx][ny] == -1:
                if b == 0:
                    for j in range(4):
                        nnx = nx + dx[i]
                        nny = ny + dy[i]
                        if nnx<= -1 or nnx >= n or nny <=-1 or nny >=m:
                            continue
                        if nnx == n - 1 and nny == m - 1:
                            return maze[x][y] + 2
                        if maze[nnx][nny] == -1:
                            continue
                        else:
                            if maze[nnx][nny] == 0 or maze[nnx][nny] >= maze[nx][ny]:
                                maze[nnx][nny] = maze[nx][ny] + 2
                                q.append((nnx,nny,1))
                else:
                    continue
            else:
                if maze[nx][ny] == 0 or maze[nx][ny] >= maze[x][y]:
                    maze[nx][ny] = maze[x][y] + 1
                    q.append((nx, ny, b))
        print(q)
    return -1

print(bfs(0,0,0, maze))



