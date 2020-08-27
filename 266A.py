def main():
    s = int(input())
    lst = input()
    count = 0
    a = lst[0]
    for i in lst[1:]:
        if i == a:
            count += 1
        a = i
    print(count)

if __name__ == "__main__":
    main()