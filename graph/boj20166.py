"""
1트: 전체 배열로는 완전탐색을 수행하고 한 좌표마다 깊이우선으로 탐색하며 중간에 글자가 달라지지 않을 경우 큐에서 제거하는 방식으로 접근
"""
import sys
input = sys.stdin.readline
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
answer_dic = {}
def find_target(x, y, target, maze):
    result = 0
    stack = []
    idx = 0
    stack.append((x,y,idx))
    l1 = len(maze)
    l2 = len(maze[0])
    while stack:
        x,y,idx = stack.pop()
        #if idx >= len(target):
        #    continue
        if maze[x][y] == target[idx]:
            if idx == len(target)-1:
                result+=1
            else:
                if idx + 1 < n:
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx == l1:
                            nx = 0
                        if nx == -1:
                            nx = l1 -1
                        if ny == l2:
                            ny = 0
                        if ny == -1:
                            ny = l2 -1
                        stack.append((nx, ny, idx+1))
    return result
n,m,k = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(input().rstrip())

for _ in range(k):
    target = input().rstrip()
    if target in answer_dic:
        print(answer_dic[target])
    else:
        result = 0
        for i in range(n):
            for j in range(m):
                result += find_target(i, j, target, maze)
                answer_dic[target] = result
        print(result)