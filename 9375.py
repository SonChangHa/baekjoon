def com(n, r):
    return fac(n) / fac(r) / fac(n - r)


for _ in range(int(input())):
    dic = {}
    for _ in range(int(input())):
        temp = input().split()
        if temp[1] not in dic:
            dic[f"{temp[1]}"] = 2
        else:
            dic[temp[1]] += 1

    temp = dic.items()
    result = 1
    for i in temp:
        result *= i[1]
    result -= 1

    print(result)
        
                   
    
