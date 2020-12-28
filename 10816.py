import sys
def put():
    return list(map(int,input().split()))
input = sys.stdin.readline

dic = {}

n = input()

nli = put()

for k in nli:
    if k in dic:
        dic[k] += 1

    else:
        dic[k] = 1

t = input()
tli = put()

for j in tli:
    if j not in dic:
        print('0', end = " ")
    else:
        print(dic[j], end = " ")
