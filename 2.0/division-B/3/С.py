def main():
    nums = list(map(int, input().split()))
    st = set()
    dup = set()
    for el in nums:
        if el in st:
            st.remove(el)
            dup.add(el)
        if el not in dup and el not in st:
            st.add(el)
    for el in nums:
        if el in st:
            print(el, end=' ')


if __name__ == '__main__':
    main()
