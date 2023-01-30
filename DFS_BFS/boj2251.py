import sys
input = sys.stdin.readline
from collections import deque


def boj2251():
    result = []
    a,b,c = map(int, input().split())
    visited = [[[False] * (c+1) for i in range(b+1)] for j in range(a+1)]
    q = deque()
    q.append((0,0,c))
    visited[0][0][c] = True
    while q:
        first,second,third = q.popleft()
        if first == 0:
            result.append(third)
        if first < a: 
            if second > 0: #b->a
                if first + second >= a:
                    if not visited[a][first+second - a][third]:
                        q.append((a, first+second - a, third))
                        visited[a][first+second - a][third] = True
                else:
                    if not visited[first+second][0][third]:
                        q.append((first+second, 0, third))
                        visited[first+second][0][third] = True
            if third > 0: #c->a
                if first + third >= a:
                    if not visited[a][second][first+third-a]:
                        q.append((a, second, first+third-a))
                        visited[a][second][first+third-a] = True
                else:
                    if not visited[first+third][second][0]:
                        q.append((first+third, second, 0))
                        visited[first+third][second][0] = True
        if second < b:
            if first > 0: #a->b
                if first + second >= b:
                    if not visited[first+second - b][b][third]:
                        q.append((first+second - b, b, third))
                        visited[first+second - b][b][third] = True
                else:
                    if not visited[0][first+second][third]:
                        q.append((0, first+second, third))
                        visited[0][first+second][third] = True
            if third > 0: #c->b
                if second + third >= b:
                    if not visited[first][b][second+third - b]:
                        q.append((first, b, second+third - b))
                        visited[first][b][second+third - b] = True
                else:
                    if not visited[first][second+third][0]:
                        q.append((first, second+third, 0))
                        visited[first][second+third][0] = True
        if third < c:
            if first > 0: #a->c
                if first + third >= c:
                    if not visited[first+third - c][second][c]:
                        q.append((first+third - c, second, c))
                        visited[first+third - c][second][c] = True
                else:
                    if not visited[0][second][first + third]:
                        q.append((0, second, first + third))
                        visited[0][second][first + third] = True
            if third > 0: #b->c
                if second + third >= c:
                    if not visited[first][second+third - c][c]:
                        q.append((first, second+third - c, c))
                        visited[first][second+third - c][c] = True
                else:
                    if not visited[first][0][second+third]:
                        q.append((first, 0, second+third))
                        visited[first][0][second+third] = True
    return result



if __name__ == "__main__":
    print(*sorted(boj2251()))

