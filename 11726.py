n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)

dp = [0] * n # [1, 2, 3, 5]
dp[0] = 1 # 손으로 계산해서 2x1일때 경우 계산
dp[1] = 2 # 마찬가지로 2x2일때 경우 계산

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1] % 10007)
