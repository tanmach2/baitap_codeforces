l = list(map(int, input().split(" ")))
lst = list(map(int, input().split(" ")))
s =l[1]-1
count = 0
for i in range(0,len(lst)):
    if lst[i] >= lst[s] and lst[i] > 0:
        count += 1
print (count)