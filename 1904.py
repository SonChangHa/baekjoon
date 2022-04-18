import sys

n = int(input())

if n == 1:
    print(1)
    sys.exit()
elif n == 2:
    print(2)
    sys.exit()

dp = [0] * n
dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746 # 그냥 하면 수가 너무 커짐.

print(dp[n-1])