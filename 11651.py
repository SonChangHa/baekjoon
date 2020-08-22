import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline



n = int(input())

li = []

for _ in range(n):
    li.append(tuple(map(int,input().split())))

li = sorted(li, key = lambda x:(x[1], x[0]))

for k in li:
    for t in k:
        print(t, end=' ')
    print("")
