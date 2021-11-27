import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

n = int(input())
a = int(input())
if a:
    a = set(input().split())
else:
    a = set()

ans = abs(100 - n)

for num in range(1000001):
    for N in str(num):
        if N in a: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(num)) + abs(num - n))

print(ans)