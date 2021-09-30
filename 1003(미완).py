import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

li = [0, 1]

def fi(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        global li
        if len(li) > n:
            return li[n]
        else:
            t = fi(n-1) + fi(n-2)
            li.append(t)
            return t

for i in range(int(input())):
    k = int(input())
    if k == 0:
        print('1','0')
    else:
        print(fi(k-1), fi(k))

