k, n = map(int, input().split())
l = []
for _ in range(k):
    l.append(int(input()))
start = 1
end = max(l)
result = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for line in l:
        tmp += line // mid
    if tmp >= n:
        start = mid + 1
    elif tmp < n:
        end = mid - 1
print(end)
