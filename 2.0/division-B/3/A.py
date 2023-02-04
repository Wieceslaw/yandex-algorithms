def main():
    st1 = set(list(map(int, input().split())))
    st2 = set(list(map(int, input().split())))
    print(len(st1.intersection(st2)))


if __name__ == '__main__':
    main()
