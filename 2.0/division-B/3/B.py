def main():
    nums = list(map(int, input().split()))
    st = set()
    for num in nums:
        if num in st:
            print("YES")
        else:
            print("NO")
            st.add(num)


if __name__ == '__main__':
    main()
