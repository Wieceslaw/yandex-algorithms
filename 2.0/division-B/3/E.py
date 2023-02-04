def main():
    m = int(input())
    witnesses = []
    for i in range(m):
        witnesses.append(set(input()))

    n = int(input())
    dct = {}
    for i in range(n):
        number = input()
        number_st = set(number)
        c = 0
        for witness in witnesses:
            if number_st.issuperset(witness):
                c += 1
        if c in dct:
            dct[c].append(number)
        else:
            dct[c] = [number]
    for el in dct[max(dct.keys())]:
        print(el)


if __name__ == '__main__':
    main()
