
channel = int(input())
str_ch = str(channel)
n = int(input())
broken = []
#new_ch = ''
if n != 0 :  broken = [str(x) for x in input().split()]

big_ch = 0
small_ch = 0
big_ch = int('1' + '0'*len(str_ch))
small_ch = int('9'* (len(str_ch)-1))

def check_go_straight(str_ch, broken):
    for num in str_ch:
        if num in broken:
            return False
    return True

def pb1107(str_ch, broken):
    if str_ch == '100':
        print(0)
        return
    if check_go_straight(str_ch, broken):
        print(len(str_ch))
        return

    combi = []
    for i in range(len(str_ch)):
        tmp = set()
        if str_ch[i] not in broken:
            tmp.add(str_ch[i])
        for j in range(int(str_ch[i])+1, 10):
            if str(j) not in broken:
                tmp.add(str(j))
                break
        for j in range(int(str_ch[i])-1, -1, -1):
            if str(j) not in broken:
                tmp.add(str(j))
                break
        combi.append(tmp)

    possible_numbers = [list(combi[0])]
    combi.pop(0)
    for item in combi:
        for num in item:
            for nums in possible_numbers:
                possible_numbers.append()

    print(combi)
    print(big_ch)
    print(small_ch)








