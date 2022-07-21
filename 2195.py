s = input()
p = input()
result = 0
while len(p)>0:
    if len(p)==1:
        result += 1
        break
    for i in range(1,len(p)+1):
        if p[:i] in s:
            continue
        else:
            p = p[i-1:]
            result += 1
            break
print(result)