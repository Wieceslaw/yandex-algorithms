def main():
    string = input()
    c = 0
    for i in range(len(string) // 2):
        start = i
        end = len(string) - i - 1
        if string[start] != string[end]:
            c += 1
    print(c)


if __name__ == '__main__':
    main()
