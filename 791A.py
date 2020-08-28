s = list(map(int, input().split(" ")))
c = 0
a = s[0]
b = s[1]
while (True):
    a = a * 3
    b = b * 2
    if a > b:
        break 
    else:
        c = c + 1
print(c+1)