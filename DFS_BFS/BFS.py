from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False for _ in range(9)]


def dfs_search(graph, node, visited):
    queue = deque([node])
    visited[node] = True

    while(queue):
        now_node = queue.popleft()
        print(now_node, end='')
        for nb in graph[now_node]:
            if visited[nb] is False:
                queue.append(nb)
                visited[nb] = True

dfs_search(graph, 1, visited)


