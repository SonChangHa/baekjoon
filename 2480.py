import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

t = put()

if t[0] == t[1] and t[1] == t[2]:
    print(10000 + t[0] * 1000)

elif t[0] != t[1] and t[1] != t[2] and t[0] != t[2]:
    print(max(t) * 100)

else:
    if t[0] == t[1] or t[0] == t[2]:
        print(1000 + t[0] * 100)
    elif t[1] == t[2]:
        print(1000 + t[1] * 100)