def main(r, i, c):
    if i == 0:
        if r != 0:
            return 3
        else:
            return c
    elif i == 1:
        return c
    elif i == 4:
        if r != 0:
            return 3
        else:
            return 4
    elif i == 6:
        return 0
    elif i == 7:
        return 1
    return i


if __name__ == '__main__':
    _r = int(input())
    _i = int(input())
    _c = int(input())
    print(main(_r, _i, _c))
