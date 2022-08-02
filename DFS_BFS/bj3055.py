from collections import deque

n,m = map(int,input().split())
maze = [list(input()) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
b_space = []
w_space = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maze[i][j] == 'S':
            b_space = [i, j]
            continue
        if maze[i][j] == '*':
            w_space.append([i, j])

visited[b_space[0]][b_space[1]] = True

def bfs(b_space, w_space, maze):
    q = deque()
    q.append((b_space, w_space, 0))
    while q:
        bs, ws, t = q.popleft()
        new_water = ws.copy()
        for w in ws: #물을 새로운 칸으로 이동
            x = w[0]
            y = w[1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                    continue
                if maze[nx][ny] == '.':
                    new_water.append([nx, ny])

        x = bs[0]
        y = bs[1]
        for i in range(4): #비버가 이동. 이동한 경로를 큐에 삽입
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if maze[nx][ny] == 'D':
                return t + 1
            if maze[nx][ny] == '.' and [nx, ny] not in new_water and visited[nx][ny] == False:
                q.append(([nx, ny],new_water, t + 1))
                visited[nx][ny] = True
    return 'KAKTUS'
                    
print(bfs(b_space,w_space,maze))
