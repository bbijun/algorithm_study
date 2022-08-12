n = int(input())
numbers = list(map(int, input().split()))
k = int(input())
for i in range(len(numbers)-1):
    if k == 0:
        break
    mx = numbers[i]
    idx = i
    for j in range(i+1, min(i+1+k, len(numbers))):
        if numbers[j] > mx:
            mx = numbers[j]
            idx = j
    k -= idx - i
    for j in range(idx, i, -1):
        numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
print(*numbers)