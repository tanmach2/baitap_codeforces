s = int(input())
list = []
k = 0
if 1<= s <= 150:
    for i in range(s):
        list.append(str(input()))
for v in list:
    if v == "++X" or v == "X++":
        k += 1
    elif v == "--X" or v == "X--":
        k -= 1
print (k)