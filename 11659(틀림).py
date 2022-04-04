n, m = list(map(int, input().split()))

nlist = list(map(int, input().split()))

for _ in range(m):
    i, j = list(map(int, input().split()))
    temp = nlist[i-1:j]
    print(sum(temp))