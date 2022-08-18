n, m = map(int, input().split())
l = list(map(int, input().split()))
start = max(l)
end = 10**9
result = sum(l)
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    tmp = 0
    for item in l:
        if tmp + item <= mid:
            tmp += item
        else:
            cnt += 1
            tmp = item
    if cnt <= m:
        end = mid - 1
        result = min(mid, result)
    else:
        start = mid + 1
print(result)