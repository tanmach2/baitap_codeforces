s = input()
a = 0           #Cchữ in thường
b = 0           #Cchữ in hoa
for c in s:
    if c.islower():
        a += 1
    elif c.isupper():
        b += 1
if a >= b:
    print(s.lower())
else:
    print(s.upper())