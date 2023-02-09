import sys
input = sys.stdin.readline
INF = int(1e9)
def boj1916():

    n = int(input().rstrip())
    m = int(input().rstrip())
    graph = [{} for _ in range(n+1)]
    visited = [False] * (n+1)
    distance = [INF] * (n+1)
    for i in range(m):
        s, d, c = map(int, input().split())
        if d in graph[s]:
            if c< graph[s][d]:
                graph[s][d] = c
        else:
            graph[s][d] = c


    start, end = map(int, input().split())
    dijstra(graph, start, visited, distance)
    return distance[end]

def get_small(distance, visited):
    smallest = INF
    result = 0
    for i in range(1, len(distance)):
        if distance[i] < smallest and not visited[i]:
            smallest = distance[i]
            result = i
    return result

def dijstra(graph, start, visited, distance):
    distance[start] = 0
    visited[start] = True
    for key in graph[start]:
        distance[key] = graph[start][key]

    for _ in range(len(graph)-2):
        now = get_small(distance, visited)
        visited[now] = True
        for key in graph[now]:
            if distance[key] > distance[now] + graph[now][key]:
                distance[key] = distance[now] + graph[now][key]


if __name__ == "__main__":
    print(boj1916())