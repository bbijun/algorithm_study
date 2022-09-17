import sys
from collections import deque
input = sys.stdin.readline
result = 0
dx = [-1,0,0,1]
dy = [0,-1,1,0]
n = int(input())
maze = []
x = y = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        x = _
        y = tmp.index(9)
    maze.append(tmp)
maze[x][y] = 0

def move(x,y, weight, maze):
    visited = [[False] * n for _ in range(n)]
    found = False
    q = deque()
    min_distance = int(10e9)
    candidate = []
    q.append((x,y,0))
    while q:
        x, y, distance= q.popleft()
        #visited[x][y] = True 44번째 줄 대신 이걸 쓰면 메모리 초과가 나는데 어차피 같은 방법 아닌가??
        if 0< maze[x][y] < weight:
            if not found:
                min_distance = distance
                found = True
                candidate.append((x, y))
            else:
                if distance == min_distance:
                    candidate.append((x, y))
        elif maze[x][y] == weight or maze[x][y] == 0:
            if distance < min_distance:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        q.append((nx,ny,distance+1))
                        visited[nx][ny] = True

    if len(candidate) == 0:
        return False, -1, -1, -1
    else:
        candidate.sort()
        return True, candidate[0][0], candidate[0][1], min_distance

weight = 2
count = 0
while True:
    flag, x, y, moves = move(x,y,weight, maze)
    if flag:
        count +=1
        result += moves
        if count == weight:
            weight +=1
            count = 0
        maze[x][y] = 0
    else:
        break
print(result)