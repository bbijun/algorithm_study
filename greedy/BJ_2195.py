s = input()
p = input()
result = 0
while len(p)>0:
    for i in range(len(p),-1,-1):
        if p[:i] in s:
            p = p[i:]
            result+=1
            break
print(result)

