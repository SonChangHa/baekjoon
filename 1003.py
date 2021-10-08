import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

li = [0, 1] #피보나치 수열 저장하는 리스트

def fi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #만약 수열 저장한 리스트에 값이 있으면
        global li
        if len(li) > n:
            return li[n] # 리스트에서 바로 값을 꺼내준다
        else: #수열 저장한 리스트에 값이 없으면
            t = fi(n-1) + fi(n-2) #정석대로 피보나치 구하기
            li.append(t) #구한 피보나치값 삽입
            return t

for i in range(int(input())):
    k = int(input())
    if k == 0:
        print('1','0')
    else:
        print(fi(k-1), fi(k)) #0과 1이 호출되는 수는 n-1번째 피보나치수, 현재 피보나치수와 동일
