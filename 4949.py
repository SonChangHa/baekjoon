import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

while True:
    k = list(input())
    k.pop()

    if k[0] == '.':
        break

    li = []

    ch = 'yes'

    for t in k:
        if t == "(" or t == "[" or t == "{":
            li.append(t)
        elif t == ")":
            if len(li) == 0:
                ch = 'no'
                break
            elif li.pop() != "(":
                ch='no'
                break

        elif t == "]":
            if len(li) == 0:
                ch = 'no'
                break
            elif li.pop() != "[":
                ch='no'
                break
        
        elif t == "}":
            if len(li) == 0:
                ch = 'no'
                break
            elif li.pop() != "{":
                ch='no'
                break
    if len(li) != 0:
        ch = 'no'
    print(ch)            
