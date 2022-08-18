import math
import sys
n, m = map(int, input().split())
l = []
for _ in range(m):
    l.append(int(input()))
start = 1
end = max(l)
result = sys.maxsize
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for item in l:
        cnt += math.ceil(item/mid)

    if cnt>n:
        start = mid + 1
    else:
        end = mid - 1
        result = min(mid, result)
print(result)
