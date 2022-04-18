import sys

t = int(input())

for _ in range(t):

    n = int(input())

    dp = [0] * n # [1, 2, 3, 5]
    dp[0] = 1 # 손으로 계산해서 2x1일때 경우 계산
    dp[1] = 2 # 마찬가지로 2x2일때 경우 계산
    dp[2] = 4

    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n-1])