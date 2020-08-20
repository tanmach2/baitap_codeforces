s = input()
lst = s.split(" ")
k = 0
if int(lst[1]) % 2 == 0:
    k = (int(lst[1]) / 2 ) * int(lst[0])
    print(int(k))
else:
    k = ((int(lst[1]) - 1) / 2 ) * int(lst[0]) + int(lst[0]) / 2
    print(int(k))