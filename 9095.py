import sys

t = int(input())

for _ in range(t):

    n = int(input())

    if n == 1:
        print(1)
        continue
    elif n == 2:
        print(2)
        continue
    elif n == 3:
        print(4)
        continue

    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n-1])