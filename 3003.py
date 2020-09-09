import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

n = put()

m = [1,1,2,2,2,8]

for i in range(len(n)):
    print(m[i] - n[i], end=' ')
