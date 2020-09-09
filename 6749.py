import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

c3 = int(input())
c2 = int(input())

print(c2 + (c2-c3))
