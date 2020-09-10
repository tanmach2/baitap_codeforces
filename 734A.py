s =  int(input())
lst = list(input())
a = 0
b = 0

for i in lst:
    if i == "A":
        a += 1
    else:
        b += 1
if a > b:
    print("Anton")
elif a < b:
    print("Danik")
else:
    print("Friendship")
