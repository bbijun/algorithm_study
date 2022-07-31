def dfs(x,y,maze,n,m):
    if x<=-1 or x>= n or y<=-1 or y>=m:
        return False
    if maze[x][y] == 0:
        return False

    if maze[x][y]==1:
        maze[x][y]=0
        dfs(x,y+1, maze,n,m)
        dfs(x+1,y, maze,n,m)
        dfs(x,y-1, maze,n,m)
        dfs(x-1,y, maze,n,m)
        return True
    return False
results = []
q = int(input())
for _ in range(q):
    n,m,k = map(int,input().split())
    maze = []
    result = 0
    for i in range(n):
        tmp = [0 for _ in range(m)]
        maze.append(tmp)

    for i in range(k):
        x, y = map(int, input().split())
        maze[x][y] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j, maze,n,m):
                result+=1
    results.append(result)
for item in results:
    print(item)
