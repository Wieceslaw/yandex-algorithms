def main():
    x, y, z = list(map(int, input().split()))
    if x > 12 or y > 12 or x == y:
        print(1)
        return
    print(0)


if __name__ == '__main__':
    main()
