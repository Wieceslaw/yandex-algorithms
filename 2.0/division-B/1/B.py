def main(n, i, j):
    return min(abs(j - i) - 1, min(j, i) + (n - max(j, i)) - 1)


if __name__ == '__main__':
    _n, _i, _j = list(map(int, input().split()))
    print(main(_n, _i, _j))
