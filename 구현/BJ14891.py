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

def check(gears, gear, direction):
    if direction == 'R':
        if gears[gear][2] != gears[gear+1][6]:
            return True
        else: return False
    if direction == 'L':
        if gears[gear][6] != gears[gear-1][2]:
            return True
        else: return False

hol = [0,2]
chack = [1,3]

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
    roll_gears = [gear]
    for j in range(gear,4):
        if j == 3:continue
        if check(gears, j, 'R'):
            roll_gears.append(j+1)
        else:
            break
    for j in range(gear,-1,-1):
        if j == 0:continue
        if check(gears, j, 'L'):
            roll_gears.append(j-1)
        else:
            break

    for roll_gear in roll_gears:
        if gear in hol:
            if roll_gear in hol:
                move(gears, roll_gear, direction)
            else:
                move(gears, roll_gear, direction * -1)
        if gear in chack:
            if roll_gear in chack:
                move(gears, roll_gear, direction)
            else:
                move(gears, roll_gear, direction * -1)

for i in range(0,4):
    score += gears[i][0] * (2**i)
print(score)

