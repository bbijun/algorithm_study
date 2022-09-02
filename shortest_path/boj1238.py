"""
플로이드로 풀었다가 시간초과나서 실패 n이 최대 1000개라 10^(3+3+3)연산으로 1초안에 될줄알았는데 아슬아슬하게
걸리는거 같음. 다익스트라로 x까지의 각 최단시간을 구하고 x부터 최단시간을 구하면 N * logN으로 풀릴거같음 다시 시도
"""

import sys
input = sys.stdin.readline
INF = int(1e9)
n, m, x = map(int, input().split())
result = 0
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(n+1):
    graph[a][a] = 0

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s][e] = t

for k in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end])
for k in range(1, n+1):
    result = max(result, graph[k][x] + graph[x][k])
print(result)