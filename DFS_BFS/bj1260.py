from collections import deque
n,m,v = map(int, input().split())
nodes = [[] for _ in range(n+1)]

for _ in range(m):
    v_1, v_2 = map(int, input().split())
    nodes[v_1].append(v_2)
    nodes[v_2].append(v_1)
for i in range(len(nodes)):
    nodes[i] = sorted(nodes[i])

visited = [False for _ in range(n+1)]

def dfs(nodes, v):
    if visited[v] is False:
        visited[v] = True
        print(v, end=' ')
        for nb in nodes[v]:
            if visited[nb] is False:
                dfs(nodes, nb)

def bfs(nodes, v):
    queue = deque()
    queue.append(v)
    while queue:
        nn = queue.popleft()
        if visited[nn] is False:
            print(nn, end=' ')
            visited[nn] = True
        for nb in nodes[nn]:
            if visited[nb] is False:
                print(nb, end=' ')
                visited[nb] = True
                queue.append(nb)
dfs(nodes, v)
print()
visited = [False for _ in range(n+1)]
bfs(nodes, v)
