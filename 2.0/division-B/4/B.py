import sys


def main():
    lines = sys.stdin.readlines()
    dct = {}
    for line in lines:
        surname, n = line.split()
        if surname in dct:
            dct[surname] += int(n)
        else:
            dct[surname] = int(n)
    for surname in sorted(dct.keys()):
        print(surname, dct[surname])


if __name__ == "__main__":
    main()
