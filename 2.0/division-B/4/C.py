import sys


def main():
    lines = sys.stdin.readlines()
    dct = {}
    mx = 0
    for line in lines:
        for word in line.split():
            if word in dct:
                dct[word] += 1
            else:
                dct[word] = 1
                mx = max(mx, dct[word])
    lst = [(mx - dct[key], key) for key in dct]
    for _, word in sorted(lst):
        print(word)


if __name__ == "__main__":
    main()
