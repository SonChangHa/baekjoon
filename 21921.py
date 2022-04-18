n, x = list(map(int, input().split()))

t = list(map(int, input().split()))

a = []
for i in range(n - x + 1):
    p = t[i:i+x]
    a.append(sum(p))


if max(a) == 0:
    print("SAD")
else:
    print(max(a))
    print(a.count(max(a)))


