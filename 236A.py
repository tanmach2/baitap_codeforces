def main():
    s = input()
    c = len(set(s))
    if c % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

if __name__ == "__main__":
    main()