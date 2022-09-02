"""
플로이드로 풀었다가 시간초과나서 실패 n이 최대 1000개라 10^(3+3+3)연산으로 1초안에 될줄알았는데 아슬아슬하게
걸리는거 같음. 다익스트라로 x까지의 각 최단시간을 구하고 x부터 최단시간을 구하면 N * logN으로 풀어서 성공
"""

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return distance


n, m, x = map(int, input().split())
result = 0
final_distance = [[0]]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,d = map(int, input().split())
    graph[s].append((d,e))

for i in range(1, n+1):
    final_distance.append(dijkstra(i))
for i in range(1, n+1):
    result = max(result, final_distance[i][x] + final_distance[x][i])
print(result)