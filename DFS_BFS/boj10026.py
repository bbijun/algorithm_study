import sys
input = sys.stdin.readline
from collections import deque

def boj10026():
    
    n = int(input().rstrip())
    maze_RGB = []
    maze_RB = []
    for _ in range(n):
        tmp = input().rstrip()
        maze_RGB.append(list(map((lambda x: [x,False]), tmp)))
        maze_RB.append(list(map((lambda x: ['R',False] if x=='G' else [x, False]), tmp)))
    
    result = [bfs(maze_RGB), bfs(maze_RB)]
    return result

def bfs(maze):
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]

    q = deque()
    q.append((0,0))
    maze[0][0][1] = False
    n = len(maze)
    result = 0
    for i in range(n):
        for j in range(n):
            if not maze[i][j][1]:
                result += 1
                q.append((i,j))
                maze[i][j][1] = True
                color = maze[i][j][0]
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if -1<nx< n and -1<ny<n:
                        if not maze[nx][ny][1] and maze[nx][ny][0] == color:
                            q.append((nx,ny))
                            maze[nx][ny][1] = True
    return result    

if __name__ == '__main__':
    print(*boj10026())
