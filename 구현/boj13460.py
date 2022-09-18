"""
1트: visited를 red_visited 2차원, blue_visited 2차원 배열로 각각 구현했음
2트: 1트처럼하면 안되는 반례가 있었음.B를 어느 위치에 고정시키고 R을 다시 구멍에 넣기위해 돌아올 때
이미 방문한 곳이라 예외처리로 이동하지 않는 문제가 있었음
-> R과 B가 동시에!! 움직이기 때문에 이런 경우는 visited를 함께 묶어서 4차원 배열로 사용해야함
[red_x][red_y][blue_x][blue_y] 이런식으로. 새로운거 하나 배웠음
"""
import sys
from collections import deque

input = sys.stdin.readline

red = []
blue = []
n, m = map(int, input().split())
maze = []
result = -1
dx = [-1, 1, 0, 0]  # U D L R
dy = [0, 0, -1, 1]

def roll(loc, path, maze):
    ball_flag = False
    hole_flag = False
    x = loc[0]
    y = loc[1]
    nx = x + dx[path]
    ny = y + dy[path]
    while maze[nx][ny] != '#':
        if maze[nx][ny] == 'O':
            hole_flag = True
        if maze[nx][ny] == 'R' or maze[nx][ny] == 'B':
            ball_flag = True
        x = nx
        y = ny
        nx += dx[path]
        ny += dy[path]
    if hole_flag:
        return [-1, -1], True
    if ball_flag:
        return [x - dx[path], y - dy[path]], False
    else:
        return [x, y], False


for _ in range(n):
    tmp = input().rstrip()
    if 'R' in tmp:
        red.append(_)
        red.append(tmp.find('R'))
    if 'B' in tmp:
        blue.append(_)
        blue.append(tmp.find('B'))
    maze.append(list(tmp))
#red_visited = [[False] * m for _ in range(n)] #잘못 생각한 경우임
#blue_visited = [[False] * m for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = deque()
q.append((red, blue, 0))
while q:
    red, blue, count = q.popleft()
    if count >= 10:
        continue
    if visited[red[0]][red[1]][blue[0]][blue[1]]:continue
    #if red_visited[red[0]][red[1]] and blue_visited[blue[0]][blue[1]]:continue
    visited[red[0]][red[1]][blue[0]][blue[1]] = True
    #red_visited[red[0]][red[1]] = True
    #blue_visited[blue[0]][blue[1]] = True
    maze[red[0]][red[1]] = 'R'
    maze[blue[0]][blue[1]] = 'B'

    for i in range(4):
        n_red, flag_red = roll(red, i, maze)
        n_blue, flag_blue = roll(blue, i, maze)
        if flag_red and not flag_blue:
            result = count+1
            q.clear()
            break
        #if red_visited[n_red[0]][n_red[1]] and blue_visited[n_blue[0]][n_blue[1]]:
        #    continue
        if flag_blue:
            continue
        q.append((n_red, n_blue, count + 1))
    if result != 1:
        maze[red[0]][red[1]] = '.'
        maze[blue[0]][blue[1]] = '.'

print(result)