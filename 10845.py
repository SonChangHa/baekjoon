import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline





q = []

n = int(input())

for _ in range(n):
    k = input()
    k = k.rstrip('\n')

    if 'push' in k:
        k1, k2 = k.split()
        q.insert(0, k2)

    elif k == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())

    elif k == 'size':
        print(len(q))

    elif k == 'empty':
        if len(q) == 0:
            print('1')
        else:
            print('0')

    elif k == 'front':
        if len(q) == 0:
            print('-1')
        else:
            print(q[-1])

    elif k == 'back':
        if len(q) == 0:
            print('-1')
        else:
            print(q[0])
