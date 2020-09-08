n1, n2 = list(map(int,input().split()))

n = n1 * n2

m = list(map(int,input().split()))

for r in m:
    print(r-n, end=' ')
