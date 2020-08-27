s = int(input())
list = []
if 1<= s <= 100:
    for i in range(s):
        list.append(str(input()))
for v in list:
    k = len(v)
    if 0 < k <= 10:
        print(v)
    else:
        print(v[0:1] + str(k-2) + v[-1:])