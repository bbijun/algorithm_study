import sys
input = sys.stdin.readline
from collections import defaultdict

def boj2668():
    n = int(input().rstrip())
    route = defaultdict(list)
    result = []
    for _ in range(1, n+1):
        route[_].append(int(input().rstrip()))


    for _ in range(1,n+1):
        visited = [False] *  (n+1)
        stack = [(_,0)]
        #visited[_] = True
        while stack:
            now, num = stack.pop()
            if now == _ and num != 0:
                result.append(_)
                break
            for item in route[now]:
                if not visited[item]:
                    stack.append((item, num+1))
                    visited[item] = True
    return result

if __name__ == '__main__':
    result = boj2668()
    print(len(result))
    for item in sorted(result):
        print(item)