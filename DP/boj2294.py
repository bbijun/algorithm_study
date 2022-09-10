"""
1트: a_n = min(a_n-k + 1, a_n) 점화식으로 접근
"""
n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [10001 for _ in range(m+1)]
dp[0] = 0
for coin in coins:
    for i in range(coin, m+1):
        dp[i] = min(dp[i-coin]+1, dp[i])
print(dp[m] if dp[m] != 10001 else -1)