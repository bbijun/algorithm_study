"""
1트: 위상정렬로 접근 -> 틀림
2트: 위상정렬을 하는데 목표하는 지점부터 거꾸로 가면서 각 단계에서 가장
오래걸리는 시간만 result에 더하는 방법을 사용. 그래프를 시작->도착 이 아니라 도착->시작으로 변경
"""
from collections import deque
import sys
input = sys.stdin.readline
def topological_sort(graph, indegree, build_time, k, w):
    result = 0
    if indegree[w] == 0:
        return build_time[w]
    q = deque()
    for i in range(1, k+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result += build_time[now]
        if now == w:
            return result
        for item in graph[now]:
            indegree[item] -= 1
            if indegree[item] == 0:
                q.append(item)
    return -1

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    build_time = {}
    build_tmp = list(map(int, input().split()))
    for i in range(1, n+1):
        build_time[i] = build_tmp[i-1]

    for i in range(k):
        s, e = map(int, input().split())
        graph[s].append(e)
        indegree[e] += 1
    w = int(input())
    print(topological_sort(graph, indegree, build_time,k, w))


