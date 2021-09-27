import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

def fi(n):
    global li

    if n == 0:
        global c0
        c0 += 1
        return 0
    elif n == 1:
        global c1
        c1 += 1
        return 1
    else:
        if len(li) >= n:
            return li[n-1]
        else:
            k = fi(n-1) + fi(n-2)
            li.append(k)
            return k


li = [0,1]

t = int(input())

for _ in range(t):
    c0 = 0
    c1 = 0

    n = int(input())
    fi(n)
    print(c0, c1)

# 수정 ㄱㄱ