s = int(input())
count = 0
for i in range(s):
    lst  = input()
    lst1 = lst.split(" ")
    if int(lst1[0]) < int(lst1[1]):
        count +=1
print(count)