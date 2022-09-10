"""
0 1 2 3 4 5 6 7 8 9 10
0 0 0 0 0 0 0 0 0 0 0

0 1 1 1 1 1 1 1 1 1 1

0 1 2
"""

"""1트: 아래와 같이 2차원배열로 시도했는데 메모리 터짐 로직 자체는 맞는데 메모리 허용량 때문에
1차원 배열로 만들고 덮어씌우는 방법으로 해야할듯
n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()
arry = [([0] * (m+1)) for _ in range(n)]
for i in range(n):
    arry[i][coins[i]] = 1

for i in range(n):
    for k in range(coins[i]+1,m+1):
        tmp = 0
        for j in range(i+1):
            tmp += arry[j][k-coins[i]]
        arry[i][k] = tmp
result = 0
for i in range(n):
    result += arry[i][m]
print(result)
"""
#0 1 2 3 4 5 6 7 8 9 10
#1 0 0 0 0 0 0 0 0 0 0
#1 1 1 1 1 1 1 1 1 1 1
#1 1 2 2
n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()
dp = [0 for _ in range(m+1)]
dp[0] = 1
for coin in coins:
    for i in range(coin, m+1):
        dp[i] += dp[i-coin]

print(dp[m])