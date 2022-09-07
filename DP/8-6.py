n = int(input())
arry = list(map(int, input().split()))

d = [0] * 100

d[0] = arry[0]
d[1] = max(arry[0], arry[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + arry[i])
print(d[n-1])