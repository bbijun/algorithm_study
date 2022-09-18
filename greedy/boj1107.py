def possible(m,b):
    for item in b:
        if item in m:
            return False
    return True

target = int(input())
n = int(input())
if n != 0:
    b = list(map(str, input().split()))
else:
    b = []

result = [abs(target - 100)]

flag = False
for i in range(result[0]):
    if flag:
        break
    plus = str(target + i)
    minus = str(target - i)
    if int(minus) > -1 and possible(minus, b):
        tmp = abs(int(minus) - target) + len(minus)
        result.append(tmp)
        flag = True
    if possible(plus, b):
        tmp = abs(int(plus) - target) + len(plus)
        result.append(tmp)
        flag = True
result.sort()
print(result[0])