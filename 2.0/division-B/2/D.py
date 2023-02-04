def main():
    l, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    mid = l // 2
    a_st = set(a)
    needs = set()
    if l % 2 != 0 and mid in a_st:
        needs.add(mid)
    else:
        ptr = l // 2 - 1
        while ptr >= 0:
            if ptr in a_st:
                needs.add(ptr)
                break
            ptr -= 1
        ptr = mid
        while ptr < l:
            if ptr in a_st:
                needs.add(ptr)
                break
            ptr += 1
    print(*sorted(list(needs)))


if __name__ == "__main__":
    main()
