from collections import deque

def D(num):
    num *= 2
    if num > 9999:
        return num%10000
    return num

def S(num):
    if num == 0:
        return 9999
    return num-1

def L(num):
    return num // 1000 + (num % 1000)*10

def R(num):
    return num//10 + (num % 10) * 1000

def bfs(s, d):
    q = deque()
    q.append((s, ""))
    visited = [False for _ in range(10000)]
    while q:
        n, cal = q.popleft()
        if visited[n]:
            continue
        visited[n] = True
        if n == d:
            return cal
        dn = D(n)
        if dn == d:
            return cal+"D"
        elif not visited[dn]:
            q.append((dn, cal+"D"))

        sn = S(n)
        if sn == d:
            return cal+"S"
        elif not visited[sn]:
            q.append((sn, cal+"S"))

        ln = L(n)
        if ln == d:
            return cal+"L"
        elif not visited[ln]:
            q.append((ln, cal+"L"))

        rn = R(n)
        if rn == d:
            return cal+"R"
        elif not visited[rn]:
            q.append((rn, cal+"R"))

    return -1
n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    print(bfs(s,d))