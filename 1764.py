import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

n, m = put()

d = set() #듣도 못한 사람
b = set() #보도 못한 사람

for _ in range(n):
    d.add(input())

for _ in range(m):
    b.add(input())

se = list(d & b)
se.sort()

print(len(se))
for t in se:
    print(t.rstrip())
