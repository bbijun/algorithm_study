import sys
from collections import deque
input = sys.stdin.readline

def possible(first, second, weight):
    q = deque()
    visited = [False] * (n+1)
    q.append(first)
    while q:
        now = q.popleft()
        if now == second:
            return True
        if visited[now]:
            continue
        visited[now] = True
        for next_node in b[now]:
            if b[now][next_node] > weight:
                q.append(next_node)
    return False


n, m = map(int, input().split())
b = [{} for _ in range(n+1)]
for _ in range(m):
    s, d, w = map(int, input().split())
    if d in b[s]:
        b[s][d] = max(b[s][d], w)
    else:
        b[s][d] = w
    if s in b[d]:
        b[d][s] = max(b[d][s], w)
    else:
        b[d][s] = w
s, d = map(int, input().split())
start = 1
end = 1000000001
result = 0
while start <= end:
    mid = (start + end) // 2
    if possible(s, d, mid):
        start = mid+1
    else:
        end = mid-1
print(start)
