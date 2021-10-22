a = int(input())

res = 0

for i in range(a+1):

    num1 = map(int, list(str(i)))

    cheak = i + sum(num1)

    if a == cheak:
        res = i
        break

print(res)