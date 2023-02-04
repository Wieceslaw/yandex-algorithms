def main():
    number = 1
    c = 0
    mx = 0
    while number:
        number = int(input())
        if number > mx:
            c = 0
            mx = number
        if number == mx:
            c += 1
    print(c)


if __name__ == '__main__':
    main()
