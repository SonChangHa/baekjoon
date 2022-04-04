n, k = list(map(int, input().split()))

t = list(map(int, input().split()))

max = 0
for i in range(n-k + 1):
    temp = t[i:i+k]
    if max < sum(temp):
        max = sum(temp)

print(max)
