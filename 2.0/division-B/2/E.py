def main():
    n = int(input())
    a = list(map(int, input().split()))
    sm = 0
    mx = 0
    for el in a:
        if el > mx:
            mx = el
        sm += el
    print(sm - mx)


if __name__ == "__main__":
    main()
