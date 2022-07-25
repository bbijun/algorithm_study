
channel = int(input())
n = int(input())
broken = []
if n != 0 :  broken = [str(x) for x in input().split()]

def check_broken_key_in(new_channel, broken):
    for broken_key in broken:
        if broken_key in new_channel:
            return False
    return True

def pb1107(channel, broken):
    result = 0
    if channel == 100:
        print(0)
        return
    elif check_broken_key_in(str(channel),broken) == True:
        result = min(abs(channel-100), len(str(channel)))
        print(result)
        return
    else:
        tmp = 1
        while True:
            plus = str(channel+tmp)
            minus = str(channel-tmp)
            if check_broken_key_in(plus, broken) == True:
                result = min(abs(channel-100), len(plus) + tmp)
                print(result)
                return
            if check_broken_key_in(minus, broken) == True:
                result = min(abs(channel-100), len(plus) + tmp)
                print(result)
                return
            tmp+=1
pb1107(channel, broken)


