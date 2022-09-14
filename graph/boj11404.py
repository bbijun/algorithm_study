import sys
input = sys.stdin.readline
INF = int(10e9)
n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
t = int(input())
for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
for _ in range(t):
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])
for i in range(1, n+1):
    for b in range(1, n+1):
        if graph[i][b] == INF:
            print("0", end=" ")
        else:
            print(graph[i][b], end=" ")
    print()