def main():
    n = int(input())
    children = list(map(int, input().split()))
    print(children[n // 2])


if __name__ == '__main__':
    main()
