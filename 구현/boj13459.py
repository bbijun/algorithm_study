import sys
from collections import deque
input = sys.stdin.readline

red = []
blue = []
n,m = map(int, input().split())
maze = []
result = 0
dx = [-1, 1, 0, 0] #U D L R
dy = [0, 0, -1, 1]

def check_in(loc, maze):
    x = loc[0]
    y = loc[1]
    if maze[x][y] == 'O':
        return True
    return False

def roll(color, loc, path, maze):
    x = loc[0]
    y = loc[1]
    nx = x + dx[path]
    ny = y + dy[path]
    while maze[nx][ny] == '.':
        x = nx
        y = ny
        nx += dx[path]
        ny += dy[path]
    if check_in([nx,ny],maze):
        return True, -1, -1
    else:
        return False, x, y

for _ in range(n):
    tmp = input().rstrip()
    if 'R' in tmp:
        red.append(_)
        red.append(tmp.find('R'))
        maze[_][tmp.find('R')] = '.'
    if 'B' in tmp:
        blue.append(_)
        blue.append(tmp.find('B'))
        maze[_][tmp.find('B')] = '.'
    maze.append(list(tmp))
red_visited = [[False] * m for _ in range(n)]
blue_visited = [[False] * m for _ in range(n)]

q = deque()
for i in range(1,4):
    q.append((red, blue, i))

while(q):
    red, blue, path = q.popleft()
    red_original = red[:]
    blue_original = blue[:]
    maze[red[0]][red[1]] = 'R'
    maze[blue[0]][blue[1]] = 'B'
    r1 = roll(red, path, maze)
    if r1[0]: #Red가 구멍에 들어간 경우
        maze[red[0]][red[1]] = '.'
    else:
        maze[r1[1]][r1[2]] = 'R'
        maze[red[0]][red[1]] = '.'
    b1 = roll(blue, path, maze)
    if b1[0]:
        maze[blue[0]][blue[1]] ='.'
    else:
        maze[b1[1]][b1[2]] = 'B'
        maze[blue[0]][blue[1]] = '.'


    r2 = roll(r1, path, maze)
    if r2[0]:
        maze[r1[0]][r1[0]] = '.'
    else:
        maze[r2[1]][r2[2]]= 'R'
        maze[r1[0]][r1[0]]


print(result)


