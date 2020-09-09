import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

n1, n2 = put()

n2 -= 1

print(n1*n2 + 1)
