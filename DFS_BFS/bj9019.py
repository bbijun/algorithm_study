from collections import deque

n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    visited = [False for _ in range(10000)]
    q = deque()
    q.append((s,""))

    while q:
        s, r = q.popleft()
        visited[s] = True
        if s == d:
            print(r)
            break

        ds = (2*s)%10000 #D레지스터
        if not visited[ds]:
            q.append((ds, r+"D"))
            visited[ds] = True

        ss = (s-1)%10000 #S레지스터
        if not visited[ss]:
            q.append((ss, r+"S"))
            visited[ss] = True

        ls = s // 1000 + (s % 1000)*10 #L레지스터
        if not visited[ls]:
            q.append((ls, r+"L"))
            visited[ls] = True

        rs = s//10 + (s % 10) * 1000 #R레지스터
        if not visited[rs]:
            q.append((rs, r+"R"))
            visited[rs] = True


