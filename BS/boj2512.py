n = int(input())
l = list(map(int, input().split()))
l.sort()
b = int(input())
result = 0
if sum(l) < b:
    print(l[-1])
else:
    start = 0
    end = l[-1]
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for m in l:
            if m >= mid:
                tmp += mid
            else:
                tmp += m

        if tmp <= b:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
            