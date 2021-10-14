import sys, copy
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

t = int(input())

for i in range(t):

    m, n, k = put()

    map1 = [[0 for a in range(m + 2)] for s in range(n + 2)]

    for _ in range(k):
        x, y = put()
        map1[y + 1][x + 1] = 1

    map2 = copy.deepcopy(map1)

    for i in range(n):
        for j in range(m):
            if map1[j][i] == 1:
                if map1[j+1][i] == 1:
                    map2[j][i] += 1
                if map1[j-1][i] == 1:
                    map2[j][i] += 1
                if map1[j][i+1] == 1:
                    map2[j][i] += 1
                if map1[j][i-1] == 1:
                    map2[j][i] += 1

    for t in map2:
        print(t)

