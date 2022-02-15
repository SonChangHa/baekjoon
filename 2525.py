import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

hour, min = put()
time = int(input())


min += time
while min > 59:
    min -= 60
    hour += 1

while hour > 23:
    hour -= 24

print(hour, min)