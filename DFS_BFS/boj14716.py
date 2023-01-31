import sys
from collections import deque
input = sys.stdin.readline

def boj14716():
    dx = [0,0,1,1,1,-1,-1,-1]
    dy = [1,-1,1,0,-1,1,0,-1]
    n,m = list(map(int,(input().split())))
    maze = []
    result = 0
    for _ in range(n):
        maze.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maze[i][j] != 0:
                result += 1
                q.append((i,j))
                visited[i][j]=True
                while q:
                    x,y = q.popleft()
                    for _ in range(8):
                        nx, ny = x+dx[_], y+dy[_]
                        if -1<nx<n and -1<ny<m:
                            if not visited[nx][ny] and maze[nx][ny] == 1:
                                q.append((nx,ny))
                                visited[nx][ny]= True
    return result

if __name__=='__main__':
    print(boj14716())