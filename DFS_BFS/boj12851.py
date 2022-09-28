from collections import deque
n, k = map(int, input().split())
MAX = 100001
min_distance = 0
dist = [-1] * MAX
visited = [False] * MAX
q = deque()
visited[n] = True
dist[n] = 0
q.append(n)
while q:
    now = q.popleft()
    next_node = [now*2, now + 1, now-1]
    for nxt in next_node:
        if -1<nxt<MAX and not visited[nxt]:
            q.append(nxt)
            visited[nxt] = True
            dist[nxt] = dist[now] + 1

print(dist[k])
min_distance = dist[k]
q = deque()
q.append((n,0))
result = 0
while q:
    now, step = q.popleft()
    if step > min_distance:
        continue
    if step == min_distance and now == k:
        result += 1
        continue
    if step == min_distance and now != k:
        continue
    if now * 2 < MAX:
        if dist[now * 2] >= step + 1:
            q.append((now*2, step+1))

    if now + 1 < MAX:
        if dist[now + 1] >= step + 1:
            q.append((now+1, step+1))
    if now -1 > -1:
        if dist[now - 1] >= step + 1:
            q.append((now-1, step+1))
print(result)