def main():
    s = list(map(int, input().split(" ")))
    a = 0
    for i in range(s[2]):
        a = a + (i + 1)*s[0]
    if a - s[1] >0:
        print(a - s[1])
    else:
        print(0)

if __name__ == "__main__":
    main()