# 이거 왜이러냐면 42처럼 2개씩 있는 숫자가 있어서 숫자 개수로 판단하면 안됨 슈발

t = int(input())

for _ in range(t):
    reverse = False  # R 메소드 처리용 변수
    methods = list(input())
    input()
    arr = input()
    if methods.count("D") > len(arr) // 2:
        print('error')
        continue
    left = 1  # 대괄호 제거
    right = len(arr) - 2  # 대괄호 제거


    for method in methods:
        if method == "R":
            # R 나왔으면 리버스 변수 뒤집기
            if reverse:
                reverse = False
            else:
                reverse = True
        elif method == "D":
            # D 나왔으면 리버스 체크해서 칸 당기기
            # 2씩 하는 이유는 ,가 포함되어 있기 때문
            if reverse:
                right -= 2
            else:
                left += 2



    if reverse:
        # 대충 빼놨던 대괄호 추가하고 범위 맞게 뒤집어서 출력한다는 소리
        print(f'[{"".join(reversed(arr[left:right + 1]))}]')
    else:
        # 대충 빼놨던 대괄호 추가한다는 범위 맞게 출력한다는 소리
        print(f'[{arr[left:right + 1]}]')