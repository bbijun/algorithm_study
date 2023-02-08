import sys
input = sys.stdin.readline

def boj11053():
    result = 1
    n = int(input().rstrip())
    dp = [1] * (n)
    nums = list(map(int, input().rstrip().split()))
    for i in range(1, n):
        tmp_max = 1
        for j in range(i):
            if nums[j] < nums[i] and dp[j]>= 1:
                tmp_max = max(dp[j] + 1, tmp_max)
        dp[i] = tmp_max
        if tmp_max > result:
            result = tmp_max
    return result


if __name__=="__main__":
    print(boj11053())