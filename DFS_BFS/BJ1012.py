from collections import deque
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(x,y, maze):
    if maze[x][y] == 0:
        return False
    queue = deque()
    queue.append((x,y))
    maze[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=n or nx<=-1 or ny>=m or ny<=-1:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = 0
                queue.append((nx,ny))
    return True


results = []
q = int(input())
for _ in range(q):
    n,m,k = map(int,input().split())
    maze = []
    result = 0
    for i in range(n):
        tmp = [0 for _ in range(m)]
        maze.append(tmp)

    for i in range(k):
        x, y = map(int, input().split())
        maze[x][y] = 1

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                bfs(i,j,maze)
                result+=1
    results.append(result)
for item in results:
    print(item)
