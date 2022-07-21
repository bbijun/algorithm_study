s = input()
p = input()
result = 0
while len(p) > 0:
    if len(p) == 1:
        result += 1
        break
    count = 0
    for i in range(1, len(p)+1):
        if p[:i] in s:
            #if i == len(p)-1:
            #    p = ''
            #    result += 1
            count += 1
            continue
        else:
            if count == 1:
                p = p[1:]
                result += 1
                break
            else:
                p = p[i-1:]
                result += 1
                break
print(result)