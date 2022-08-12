n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort()
result = l[0] - 1




for i in range(1,n):
    if l[i] == l[i-1] or l[i] == l[i-1] + 1:
        continue
    else:
        result += l[i] - l[i-1] -1
        l[i] = l[i-1] + 1
print(l)
print(result)
for i in range(0, n):
    result += l[i] - (i+1)
print(result)
