import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

n = input()

li = put()

li.sort()


re = 0
re2 = 0
for t in li:
    re += t
    re2 += re

print(re2)
