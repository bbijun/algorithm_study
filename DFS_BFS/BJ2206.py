from collections import deque
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x,y, broken, maze):
    q = deque()
    q.append((x,y,False))
    while q:
        x, y, b = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <=-1 or ny >=m:
                continue
            if nx == n-1 and ny == m-1:
                return visited[x][y] +1
            if maze[nx][ny] == 0 and visited[nx][ny][0] == 0 and b == False: #해당 블럭이 방문된 적이 없는 경우
                visited[nx][ny][0] = visited[x][y][0] + 1
                q.append((nx,ny, False))
            if maze[nx][ny] == 0 and visited[nx][ny][1] == 0 and b == True:
                visited[nx][ny][1] = visited[x][y][] + 1
                q.append((nx, ny, True))
            if maze[nx][ny] == 1 and visited[nx][ny][0] == 0 and b == False: #벽을 만났고 벽을 부신 적이 없는 경우
                visited[nx][ny][0] = visited[x][y][0] + 1
                q.append((nx, ny, True))

    return -1

print(bfs(0,0,False, maze))

