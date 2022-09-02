"""
1트: 생각한 방법 : start -> u -> v -> end, start -> v -> u -> end 중 작은
값이 정답일 거라는 방법으로 접근
시간초과 안날줄 알고 플로이드워셔로 시도
"""
import sys
input = sys.stdin.readline
INF = int(1e9)
n, e = map(int, input().split())
graph = [([INF] * (n+1)) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0
for _ in range(e):
    s, d, t = map(int, input().split())
    graph[s][d] = t
    graph[d][s] = t
u, v = map(int, input().split())
for k in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end])

def answer(u, v):
    result = min(graph[1][u] + graph[u][v] + graph[v][n], graph[1][v] + graph[v][u] + graph[u][n])
    if result > INF:
        return -1
    return result
print(answer(u,v))