import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False for _ in range(n+1)]
visited[1] = True
q = deque()
q.append(1)
result = 0
while q:
    node = q.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            q.append(neighbor)
            result += 1
print(result)