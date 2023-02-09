import sys
input = sys.stdin.readline

def boj11727(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    if n<3:
        return dp[n]
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]
    return dp[n] % 10007



if __name__ == "__main__":
    n = int(input().rstrip())
    print(boj11727(n))
    