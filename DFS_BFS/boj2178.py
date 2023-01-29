import sys
from collections import deque
input = sys.stdin.readline
dx = [1,0,0,-1]
dy = [0,1,-1,0]
def boj2178():
    n, m = map(int, input().split())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input().rstrip())))
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0,0,1))
    visited[0][0] = True
    while q:
        x,y,k = q.popleft()
        if x == n-1 and y == m-1:
            return k
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<n and -1<ny<m:
                if not visited[nx][ny] and maze[nx][ny] == 1:
                    q.append((nx, ny, k+1))
                    visited[nx][ny] = True
    return -1
if __name__ == "__main__":
    print(boj2178())