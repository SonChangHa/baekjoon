import sys
def put():
    return list(map(int,input().split()))
input = sys.stdin.readline #얘는 개행문자도 포함함. 주의

n = int(input())

k1, k2 = 0, 0

for i in range(0, n + 1):
    k2 += i
    
    if k1 < n <= k2:
        break

    k1 = k2

if i % 2 == 0:
    li = [1,i]
    t = n - k1 - 1
    li[0] += t
    li[1] -= t

else:
    li = [i,1]
    t = n - k1 - 1
    li[1] += t
    li[0] -= t

print(f"{li[0]}/{li[1]}")
