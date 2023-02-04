def main():
    n = int(input())
    dct = {}
    for _ in range(n):
        d, a = list(map(int, input().split()))
        if d in dct:
            dct[d] += a
        else:
            dct[d] = a
    for d in sorted(dct.keys()):
        print(d, dct[d])


if __name__ == "__main__":
    main()
