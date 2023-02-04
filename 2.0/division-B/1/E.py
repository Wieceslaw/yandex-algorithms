def main():
    d = int(input())
    x, y = list(map(int, input().split()))
    if x < 0 or y < 0 or y > -x + d:
        r = lambda cords: ((cords[0] - x) ** 2 + (cords[1] - y) ** 2) ** 0.5
        nearest = min([(0, 0), (d, 0), (0, d)], key=r)
        if nearest == (0, 0):
            print(1)
        elif nearest == (d, 0):
            print(2)
        else:
            print(3)
        return
    print(0)


if __name__ == '__main__':
    main()
