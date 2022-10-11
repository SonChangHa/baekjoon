n = int(input())

arr = []
for i in range(n):
    arr.append(tuple(map(int,input().split())))

arr.sort(key = lambda x : (x[1], x[0]))

result = [arr[0]]
for i in range(1, len(arr)):
    if arr[i][0] >= result[-1][1]:
        result.append(arr[i])

print(len(result))