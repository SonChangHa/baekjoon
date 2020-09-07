import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

m, n = put()

print(m // n)
print(m % n)
