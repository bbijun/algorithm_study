"""
1트: 생각한 방법 : start -> u -> v -> end, start -> v -> u -> end 중 작은
값이 정답일 거라는 방법으로 접근
시간초과 안날줄 알고 플로이드워셔로 시도

2트: 다익스트라로 start -> u, start -> v, u->v, v->u, u->end, v->end 구해서
정답 도출시도 85%에서 틀렸습니다 나오는데 이유를 모르겠음 여러 반례를 넣어봐도 잘 작동하는데

3트: 다익스트라 함수에서 distance배열을 선언하고 distance[start]를 0으로 수정해주지않아서
틀린거였음
"""

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
def dijkstra(start, end):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
    return distance[end]

for _ in range(e):
    a,b,s = map(int, input().split())
    graph[a].append((b,s))
    graph[b].append((a,s))
u, v = map(int, input().split())

su = dijkstra(1, u)
sv = dijkstra(1, v)
uv = dijkstra(u, v)
vu = dijkstra(v, u)
ue = dijkstra(u, n)
ve = dijkstra(v, n)
result = min(su + uv + ve, sv+ vu + ue)
if result >= INF:
    print(-1)
else:
    print(result)