def change_dice(dice, move):
    new_dice = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]
    ]
    if move == 1:
        new_dice[0][1] = dice[0][1]
        new_dice[2][1] = dice[2][1]
        new_dice[1][0] = dice[1][1]
        new_dice[1][1] = dice[1][2]
        new_dice[1][2] = dice[3][1]
        new_dice[3][1] = dice[1][0]
    elif move == 2:
        new_dice[0][1] = dice[0][1]
        new_dice[2][1] = dice[2][1]
        new_dice[1][0] = dice[3][1]
        new_dice[1][1] = dice[1][0]
        new_dice[1][2] = dice[1][1]
        new_dice[3][1] = dice[1][2]
    elif move == 3:
        new_dice[1][0] = dice[1][0]
        new_dice[1][2] = dice[1][2]
        for i in range(1,4):
            new_dice[i][1] = dice[i-1][1]
        new_dice[0][1] = dice[3][1]
    elif move == 4:
        new_dice[1][0] = dice[1][0]
        new_dice[1][2] = dice[1][2]
        for i in range(2,-1,-1):
            new_dice[i][1] = dice[i+1][1]
        new_dice[3][1] = dice[0][1]
    return new_dice

n,m, x, y, k = map(int, input().split())
board = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move_dic = {1: 0, 2: 1, 3: 2, 4: 3}
dice = [
    [-1,0,-1],
    [0,0,0],
    [-1,0,-1],
    [-1,0,-1]
]

for i in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

moves = list(map(int, input().split()))

for move in moves:
    new_x = x + dx[move_dic[move]]
    new_y = y + dy[move_dic[move]]

    if new_x < 0 or new_x >=n or new_y < 0 or new_y >= m:
        continue
    x = new_x
    y = new_y
    dice = change_dice(dice, move)
    if board[x][y] == 0:
        board[x][y] = dice[1][1]
    else:
        dice[1][1] = board[x][y]
        board[x][y] = 0
    print(dice[3][1])


