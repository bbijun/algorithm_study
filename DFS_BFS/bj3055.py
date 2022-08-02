from collections import deque

n,m = map(int,input().split())
maze = [list(input()) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[False for _ in range(m)] for _ in range(n)]

#고슴도치 시작 위치 설정
s_x = 0
s_y = 0

for i in range(n):
    for j in range(m):
        if maze[i][j] == 'S' or maze[i][j] == 'X' or maze[i][j] == '*':
            visited[i][j] = True
        if maze[i][j] == 'S':
            s_x = i
            s_y = j

#bfs 탐색
def bfs(x, y, maze): #고슴도치의 시작 위치와 미로를 입력
    q = deque()
    q.append((x, y, 0))
    while q:
        move_water(maze) #물을 먼저 이동시킨다
        for _ in range(len(q)): #현재 큐에 있는 내용만! 루프를 돌려서 고슴도치를 이동시킨다 이게 끝나면 다음 턴이 돼서 물이 또 이동한다
            x, y, t = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                    continue
                if maze[nx][ny] == 'D': return t+1 #도착지점
                if not visited[nx][ny]: #물이 차있거나 방문한 곳의 visited는 어차피 true이니까 둘이 같이 취급한다
                    q.append((nx, ny, t+1)) #한칸 이동시키고 이동한 경우 큐에 추가
                    visited[nx][ny] = True
    return 'KAKTUS' #길이 없는 경우

#물 이동 함수
def move_water(maze):
    water_space = [] #현 시점에서 물이 차있는 곳의 위치를 확인해서 water_space에 저장
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '*':
                water_space.append([i, j])
    for water in water_space: #water_space를 순회하며 물을 한칸씩 추가해준다. 물이 추가된 곳의 visited도 True로 변경
        x = water[0]
        y = water[1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx <= -1 or nx >= n or ny <= -1 or ny >=m:
                continue
            if maze[nx][ny] == '.':
                maze[nx][ny] = '*'
                visited[nx][ny] = True

print(bfs(s_x, s_y, maze))
