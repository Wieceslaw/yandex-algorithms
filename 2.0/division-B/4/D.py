import re
import sys


def main():
    lines = sys.stdin.readlines()
    sm = 0
    count = 450
    names = []
    dct = {}
    dct2 = {}
    dct3 = {}
    for line in lines:
        name, number, _ = re.split(r"(\s\d+)$", line.strip())
        names.append(name)
        number = int(number)
        sm += number
        if name in dct:
            dct[name] += number
        else:
            dct[name] = number
    first = sm / count
    for party in dct:
        dct3[party] = dct[party] // first
        count -= dct[party] // first
        d = dct[party] / first % 1
        if dct[party] / first in dct2:
            dct2[d].append(party)
        else:
            dct2[d] = [party]
    if count:
        for key in sorted(dct2.keys(), reverse=True):
            parties = dct2[key]
            for party in sorted(parties, key=lambda x: dct[x], reverse=True):
                if count:
                    dct3[party] += 1
                    count -= 1
                else:
                    break
            if not count:
                break
    for name in names:
        print(name, int(dct3[name]))


if __name__ == "__main__":
    main()
