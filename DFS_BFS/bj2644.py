from collections import deque
n = int(input())
s, d = map(int, input().split())
k = int(input())
r = [[] for _ in range(n+1)] #연관을 나타내는 그래프
visited = [False for _ in range(n+1)]
for _ in range(k):
    v_1, v_2 = map(int, input().split())
    r[v_1].append(v_2)
    r[v_2].append(v_1)


def bfs(v1, v2):
    q = deque()
    q.append((v1,0))
    while q:
        n, t = q.popleft()
        visited[n] = True
        for nb in r[n]:
            if nb == v2:
                return t+1
            if not visited[nb]:
                q.append((nb, t+1))
    return -1

print(bfs(s, d))


