import math

n = int(input())
result = math.factorial(n)

cnt = 0
while result % 10 == 0:
    result = result // 10
    cnt += 1

print(cnt)