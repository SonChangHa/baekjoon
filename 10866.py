import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

from collections import deque

d = deque()

n = int(input())

for _ in range(n):
    k = input()
    k = k.rstrip('\n')

    if 'push' in k:
        k1, k2 = k.split()
        if 'front' in k:
            d.append(k2)
        else:
            d.appendleft(k2)

    elif 'pop' in k:
        if len(d) != 0:
            if 'front' in k:
                t = d.pop()
                print(t)
            else:
                t = d.popleft()
                print(t)
        else:
            print('-1')

    elif k == 'size':
        print(len(d))

    elif k == 'empty':
        if len(d) == 0:
            print('1')
        else:
            print('0')

    elif k == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])

    elif k == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
