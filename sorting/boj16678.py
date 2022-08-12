n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort()
result = l[0] - 1
l[0] = 1
for i in range(1, n):
    if l[i] > l[i-1]+1:
        result += l[i] - (l[i-1] + 1)
        l[i] = l[i-1] + 1
print(result)
