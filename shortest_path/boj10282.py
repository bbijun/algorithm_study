import sys
import heapq
def dijkstra(graph, start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    infected = 0
    max_idx = 0
    for _ in range(1, n+1):
        if distance[_] != INF:
            infected+=1
            max_idx = max(distance[_], max_idx)
    print(infected, max_idx)
INF = int(1e9)
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    for k in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a, s))
    dijkstra(graph, c, distance)

