import sys
from collections import deque
input = sys.stdin.readline

class Ball:
    def __init__(self, name, x, y, n, m):
        self.name = name
        self.x = x
        self.y = y
        self.isin = False
        self.visited = [[False] * m for _ in range(n)]
    def Roll(self, p, maze):
        dx = [-1, 1, 0, 0] #Up Down Left Right
        dy = [0, 0, -1, 1]
        if self.isin:
            return
        while maze[self.x + dx[p]][self.y + dy[p]] == '.':
            maze[self.x][self.y] = '.'
            self.x += dx[p]
            self.y += dy[p]
        if maze[self.x + dx[p]][self.y + dy[p]] == 'O':
            self.isin = True
        if self.isin:
            maze[self.x][self.y] = '.'
        else:
            maze[self.x][self.y] = self.name
            self.visited[self.x][self.y] = True



n,m = map(int, input().split())
maze = []
red = Ball('R',0,0,n,m)
blue = Ball('B',0,0,n,m)
for _ in range(n):
    tmp = input().rstrip()
    if 'R' in tmp:
        red.x = _
        red.y = tmp.find('R')
    if 'B' in tmp:
        blue.x = _
        blue.y = tmp.find('B')
    maze.append(list(tmp))
#red.visited[red.x][red.y] = True
#blue.visited[blue.x][blue.y] = True
result = 0


q = deque()
q.append((0, 1))
q.append((1,1))
q.append((2,1))
q.append((3,1))
while(q):
    path, count = q.popleft()
    if count > 10:
        continue
    red.Roll(path, maze)
    blue.Roll(path, maze)
    if red.isin and not blue.isin:
        result = 1
        break
    blue.Roll(path, maze)
    red.Roll(path, maze)
    if blue.isin:
        continue
    if not red.visited[red.x][red.y] or not blue.visited[blue.x][blue.y]:
        for i in range(4):
            q.append((i, count+1))
print(result)


