import sys
input = sys.stdin.readline
n = int(input())
board = [list(input().strip()) for _ in range(n)]
def check_board():
    row_value = 0
    col_value = 0
    for line in board:
        for i in range(len(line)-1):
            j = i+1
            cnt = 1
            while line[i] == line[j]:
                cnt += 1
                if j == n-1:
                    break
                else:j+=1
            row_value = max(cnt, row_value)

    transpose = (zip(*board))
    for line in transpose:
        for i in range(len(line)-1):
            j = i+1
            cnt = 1
            while line[i] == line[j]:
                cnt += 1
                if j == n-1:
                    break
                else:j+=1
            col_value = max(cnt, col_value)
    return max(row_value, col_value)

result = 0


for x in range(n):
    for y in range(n):
        nx = x + 1
        ny = y + 1
        if nx<n and board[nx][y] != board[x][y]:
            board[nx][y], board[x][y] = board[x][y], board[nx][y]
            result = max(result, check_board())
            board[nx][y], board[x][y] = board[x][y], board[nx][y]
        if ny<n and board[x][ny] != board[x][y]:
            board[x][ny], board[x][y] = board[x][y], board[x][ny]
            result = max(result, check_board())
            board[x][ny], board[x][y] = board[x][y], board[x][ny]
print(result)
