s = int(input())
c = 0
while(s>0):
    s -= 1
    lst = list(map(int, input().split(" ")))
    if lst.count(int(1)) >= 2:
        c += 1
print(c)
