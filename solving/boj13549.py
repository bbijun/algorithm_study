from collections import deque
n, k = map(int, input().split())
dist = [-1] * 100001
visited = [False] * 100001
q = deque()
q.append(n)
visited[n] = True
dist[n] = 0
while q:
    now = q.popleft()
    next_node = [now * 2, now + 1, now - 1]
    if now * 2 < 100001 and not visited[now * 2]:
        q.appendleft(now * 2)
        visited[now * 2] = True
        dist[now * 2] = dist[now]

    if now + 1 < 100001 and not visited[now + 1]:
        q.append(now + 1)
        visited[now + 1] = True
        dist[now + 1] = dist[now] + 1

    if now - 1 > -1 and not visited[now - 1]:
        q.append(now - 1)
        visited[now - 1] = True
        dist[now - 1] = dist[now] + 1

print(dist[k])