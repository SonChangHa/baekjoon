import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

N = int(input())

def star(x):
    a = 1
    b = 2
    x = a + b
    return x

print(star(10))
