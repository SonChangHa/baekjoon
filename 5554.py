import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

n = 0

for _ in range(4):
    n += int(input())

print(n // 60)

n = n % 60

print(n)
