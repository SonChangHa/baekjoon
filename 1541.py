n = input()

arr = n.split("-")

for i in range(len(arr)):
    if "+" in arr[i]:
        temp = sum(list(map(int,arr[i].split("+"))))
        arr[i] = temp
arr = list(map(int, arr))

result = arr[0]
for i in range(1,len(arr)):
    result -= arr[i]

print(result)