t = int(input())
def bs(l, target):
    start = 0
    end = len(l)-1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == target:
            return mid
        elif l[mid]<target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

for _ in range(t):
    n = int(input())
    one = list(map(int, input().split()))
    one.sort()
    m = int(input())
    two = list(map(int, input().split()))
    for num in two:
        if bs(one, num) == -1:
            print(0)
        else:
            print(1)