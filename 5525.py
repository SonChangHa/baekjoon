n = int(input())
m = int(input())

text = input()

many = 0
p = 0

i = 0
while i < m-1:
    if text[i-1] == "I" and text[i] == "O" and text[i+1] == "I":
        p += 1
        if p == n:
            p -= 1
            many += 1
        i += 1
    else:
        p = 0
    i += 1

print(many)

