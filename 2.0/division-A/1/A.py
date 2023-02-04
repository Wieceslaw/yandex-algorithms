def main(a, b, c, d):
    if c and a:
        if b / a == d / c:
            print("NO")
            return

    if not a:
        if b == 0:
            print("INF")
        else:
            print("NO")
        return
    else:
        x = -b / a
        if x != int(x):
            print("NO")
        else:
            print(int(x))
        return


if __name__ == '__main__':
    _a = int(input())
    _b = int(input())
    _c = int(input())
    _d = int(input())

    main(_a, _b, _c, _d)
