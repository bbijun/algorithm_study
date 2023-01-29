import sys
from collections import deque, defaultdict
input = sys.stdin.readline
def boj2667():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = []
    maze = []
    n = int(input().rstrip())
    apart = [[0] * n for _ in range(n)]
    for _ in range(n):
        maze.append(list(map(int, input().rstrip())))
    
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 1:
                q = deque()
                q.append((i,j))
                maze[i][j] = 2
                size = 0
                while q:
                    x,y = q.popleft()
                    size += 1
                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]
                        if -1<nx<n and -1<ny<n:
                            if maze[nx][ny] == 1:
                                maze[nx][ny] = 2
                                q.append((nx,ny))
                                #size += 1
                result.append(size)
    return sorted(result)



if __name__=="__main__":
    result = boj2667()
    print(len(result))
    for item in result:
        print(item)