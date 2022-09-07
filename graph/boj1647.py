"""
1트: 크루스칼로 최소신장트리를 만든다음에 그 중에 가장 큰 비용의 엣지를
제거한 것을 결과값으로 설정
"""
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

import sys
input = sys.stdin.readline
edges = []
result = 0
v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(len(parent)):
    parent[i] = i
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()
max_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = max(max_cost, cost)
print(result - max_cost)