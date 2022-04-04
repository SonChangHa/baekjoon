n = int(input())

max = 0
for _ in range(n):
    t = sorted(list(map(int, input().split())))
    temp = set(t)

    if len(temp) == 1:
        result = 50000 + t[0] * 5000

    elif len(temp) == 2:
        if t[1] == t[2]:
            result = 10000 + t[1] * 1000
        else:
            result = 2000+ t[1] * 500 + t[2] * 500

    elif len(temp) == 3:
        for i in range(3):
            if t[i] == t[i+1]:
                result = 1000 + t[i] * 100
                break

    else:
        result = t[0] * 100

    if max < result:
        max = result


print(max)

