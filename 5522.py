import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

n = 0

for _ in range(5):
    n += int(input())

print(n)
