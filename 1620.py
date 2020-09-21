import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

n, m = put()

dic = {}


for i in range(1, n+1):
    k = input()
    dic[k] = i
    dic[i] = k

for _ in range(m):
    try:
        t = input()
        t = int(t)
        print(dic[t].rstrip())
    except ValueError as a:
        print(dic[t])
