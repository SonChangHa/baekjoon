import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

n = int(input())
arr = [0] * (n + 1)
arr[1] = 1
for i in range(2,n+1):
    arr[i] = arr

