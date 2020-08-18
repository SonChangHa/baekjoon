import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

d = []
n = int(input())

for _ in range(n):
    k = input()
    k = k.rstrip('\n')

    if 'push' in k:
        k1, k2 = k.split()
        d.append(k2)

    elif 'pop' in k:
        if len(d) != 0:
            t = d.pop()
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

    elif k == 'top':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
