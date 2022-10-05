import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
x1 = -1
y1 = -1
x2 = -1
y2 = -1
maze = []
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
for _ in range(n):
    maze.append(list(input().rstrip()))
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'o':
            if x1 == -1:
                x1 = i
                y1 = j
            else:
                x2 = i
                y2 = j
maze[x1][y1] = '.'
maze[x2][y2] = '.'
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
q.append((x1,y1,x2,y2,0))
def solution(q):
    result = -1
    while q:
        cx1, cy1, cx2, cy2, cnt = q.popleft() #cx = current x, cy = current y
        if cnt >= 10 or visited[cx1][cy1][cx2][cy2]:
            continue
        visited[cx1][cy1][cx2][cy2] = True

        for i in range(4):
            nx1 = cx1 + dx[i]
            ny1 = cy1 + dy[i]
            nx2 = cx2 + dx[i]
            ny2 = cy2 + dy[i]
            if nx1 >= n or nx1 < 0 or ny1 >= m or ny1 < 0:
                if -1<nx2<n and -1<ny2<m: #구슬 1만 떨어지는 경우
                    result = cnt + 1
                    return result
                else: #둘 다 떨어지는 경우
                    continue
            if nx2 >= n or nx2 < 0 or ny2 >= m or ny2 < 0:
                if -1<nx1<n and -1<ny1<m: #구슬 2만 떨어지는 경우
                    result = cnt + 1
                    return result
                else: #둘 다 떨어지는 경우
                    continue
            if -1<nx1<n and -1<ny1<m and -1<nx2<n and -1<ny2<m: #둘 다 안떨어지는 경우
                if visited[nx1][ny1][nx2][ny2]:
                    continue
                if maze[nx1][ny1] != '.':
                    nx1,ny1 = cx1, cy1
                if maze[nx2][ny2] != '.':
                    nx2, ny2 = cx2, cy2
                q.append((nx1,ny1,nx2,ny2, cnt+1))
    return result
print(solution(q))