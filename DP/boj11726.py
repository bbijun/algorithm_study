import sys
input = sys.stdin.readline
def boj11726(n):
    dp = [0] * (1001)
    dp[1] = 1
    dp[2] = 2
    if n<=2:
        return dp[n]
    for _ in range(3, 1001):
        dp[_] = dp[_-1] + dp[_-2]
    
    return dp[n] % 10007

if __name__=="__main__":
    n = int(input().rstrip())
    print(boj11726(n))