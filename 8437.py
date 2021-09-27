import itertools
import sys


def put():
    return list(map(int, input().split()))


input = sys.stdin.readline

a = int(input())

b = int(input())

print((a + b) // 2)
print((a - b) // 2)
