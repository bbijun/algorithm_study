"""
크루스칼 알고리즘 적용하면 그냥 풀림
"""
import sys
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

input = sys.stdin.readline
edges = []
v = int(input())
parent = [0] * (v+1)
for i in range(len(parent)):
    parent[i] = i
e = int(input())
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)