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
    visited[node] = True
    print(node, end='')
    for nb in graph[node]:
        if visited[nb] is False:
            dfs_search(graph, nb, visited)

dfs_search(graph, 1, visited)