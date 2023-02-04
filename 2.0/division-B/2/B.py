def main():
    numbers = input().split()
    homes = []
    shops = []
    for i, el in enumerate(numbers):
        if el == "2":
            shops.append(i)
        elif el == "1":
            homes.append(i)
    mx = 0
    for home in homes:
        nearest = shops[0]
        for shop in shops:
            if abs(shop - home) < abs(nearest - home):
                nearest = shop
        mx = max(mx, abs(home - nearest))
    print(mx)


if __name__ == '__main__':
    main()
