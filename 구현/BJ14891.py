def move(gears, gear, direction):
    changed_gear = [0,0,0,0,0,0,0,0]
    if direction == 1:
        for i in range(1,8):
            changed_gear[i] = gears[gear][i-1]
        changed_gear[0] = gears[gear][7]
    else:
        for i in range(0,7):
            changed_gear[i] = gears[gear][i+1]
        changed_gear[7] = gears[gear][0]
    gears[gear] = changed_gear


def check_nh(gears, gear, direction = -1):
    if direction == -1:
        if gear>0:
            if gears[gear][6] != gears[gear-1][2]:
                return True
            else:
                return False
    else:
        if gear<3:
            if gears[gear][2] != gears[gear+1][6]:
                return True
            else:
                return False

score = 0
gears = []
for i in range(4):
    string = input()
    tmp = []
    for num in string:
        tmp.append(int(num))
    gears.append(tmp)

n = int(input())
for i in range(n):
    gear, direction = map(int, input().split())
    gear-=1
    move(gears, gear, direction)
    if gear == 0:
        for j in range(3):
            if check_nh(gears, gear, 1):
                direction *= -1
                gear+=1
                move(gears, gear, direction)
            else:
                break
    elif gear == 3:
        for j in range(3):
            if check_nh(gears, gear, -1):
                direction *= -1
                gear-=1
                move(gears, gear, direction)
            else:
                break
    elif gear == 1:
        if check_nh(gears, gear, -1):
            move(gears, gear-1, direction * -1)
        for j in range(2):
            if check_nh(gears, gear, 1):
                direction *= -1
                gear += 1
                move(gears, gear, direction)
            else:
                break
    elif gear == 2:
        if check_nh(gears, gear, 1):
            move(gears, gear+1, direction * -1)
        for j in range(2):
            if check_nh(gears, gear, -1):
                direction *= -1
                gear -= 1
                move(gears, gear, direction)
            else:
                break
    
if gears[0][0] == 1:
    score += 1
if gears[1][0] == 1:
    score += 2
if gears[2][0] == 1:
    score += 4
if gears[3][0] == 1:
    score += 8

print(score)

