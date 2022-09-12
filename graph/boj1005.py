"""
1트: 위상정렬로 접근 -> 틀림
2트: 위상정렬을 하는데 목표하는 지점과 관계없는 노드는 방문하지 말아야함
따라서 위상정렬을 하기 전에 경로를 거꾸로 거슬러가며 방문할 필요가 있는 노드만 따로 보관한다
예제 1의 경우 7번 노드를 가기 위해 1,2,3,5,6의 노드만 방문하면 된다.
또한 indegree가 0인 노드가 여러개라면 그 중 가장 큰 시간이 필요한 것만 result에 추가한다.
건물을 동시에 짓는게 가능하기 때문이다.
3트: 2트가 뭔가 자꾸 안되는거같아서 알고리즘 분류를 봤음. dp가 있길래 위상정렬 + dp를 섞어봄
"""
from collections import deque
import sys
input = sys.stdin.readline

def topological_sort(graph, indegree, build_time, k, w, visit):
    result = 0
    step = []
    if indegree[w] == 0:
        return build_time[w]
    q = []
    tmp = 0
    for i in range(1, w+1):
        if indegree[i] == 0 and i in visit:
            q.append(i)
            tmp = max(build_time[i], tmp)
    result += tmp
    tmp2 = []
    while q:
        result_tmp = 0
        for item in q:
            if item in visit and item not in tmp2:
                tmp2.append(item)
                result_tmp = max()


    return -1 #불가능한 경우

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    graph_reverse = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    build_time = {}
    build_tmp = list(map(int, input().split()))
    for i in range(1, n+1):
        build_time[i] = build_tmp[i-1]

    for i in range(k):
        s, e = map(int, input().split())
        graph_reverse[e].append(s)
        graph[s].append(e)
        indegree[e] += 1
    w = int(input())
    q = deque()
    q.append(w)
    visit = [] #방문해야하는 노드. indegree가 0이어도 visit의 원소가 아니면 거른다
    while q:
        now = q.popleft()
        if now not in q:
            visit.append(now)
        for item in graph_reverse[now]:
            if item not in q:
                q.append(item)

    #print(topological_sort(graph, indegree, build_time,k, w, visit))


