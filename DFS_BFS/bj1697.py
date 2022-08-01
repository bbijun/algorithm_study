from collections import deque
s, d = map(int, input().split())

def bfs(start, destination, maze):
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        if now == destination:
            return maze[now]
        for test in (now-1, now+1, now*2):
            if test<100001 and test>-1:
                if maze[test] == 0:
                    maze[test] = maze[now]+1
                    queue.append(test)

maze = [0 for _ in range(100001)]
print(bfs(s, d, maze))