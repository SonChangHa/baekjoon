import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

r1, s = put()

r2 = (s*2) - r1

print(r2)
