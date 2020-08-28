s = list(map(int, input().split(" ")))
n = s[0]
k = s[1]

for i in range (k):
    if n % 10 != 0:
        n = n - 1
    else:
        n = n / 10
print (int(n))

    