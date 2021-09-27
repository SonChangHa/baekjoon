import itertools
import sys


def put():
    return list(map(int, input().split()))


input = sys.stdin.readline

mo = ('a', 'e', 'i', 'o', 'u')

l, c = put()  # 각 l과 c를 받음

t = input().split()  # 각 단어를 받음

mo_ = []  # 제시된 모음
etc = []  # 자음

for i in t:
    if i in mo:
        mo_.append(i)  # 모음이면 mo_배열에 넣는다
    else:
        etc.append(i)  # 자음이면 etc 배열에 넣는다

# 모든 모음의 조합을 temp 배열에 넣는다. 예를 들면 a, i가 있을경우, 각각 a / i / a,i 3개로 나누어질 것이다.
temp = []
for i in range(1, l - 1):
    for j in list(itertools.combinations(mo_, i)):
        temp.append(j)

# 모음 조합의 개수만큼 반복하면서 자음의 조합을 구한다.
temp2 = []
for i in temp:
    k = len(i)
    for j in list(itertools.combinations(etc, l - k)):
        temp2.append(i + j)

# 위에서 구한 모음과 자음 조합을 가공하여 문제에서 원하는 1문단의 형태로 바꾼다. (이걸 안하면 ['a', 'i', 'e', 'c'] 이런식으로 나옴)
for i in range(len(temp2)):
    temp2[i] = list(temp2[i])
    temp2[i].sort()
    temp2[i] = ''.join(temp2[i])

temp2.sort()

# 출력 가즈아~
for i in temp2:
    print(i)
