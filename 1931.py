n = int(input())

arr = []
for i in range(n):
    arr.append(tuple(map(int,input().split())))

arr.sort(key = lambda x : (x[1], x[0]))

result = [arr[0]]
for item in arr:
    if item[0] >= result[-1][1]:
        result.append(item)


print(len(result))