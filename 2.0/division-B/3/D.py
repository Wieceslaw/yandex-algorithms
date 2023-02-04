import sys


def main():
    n = int(input())
    st = set(range(1, n + 1))
    diff_st = set()
    while sys.stdin.readable():
        line = sys.stdin.readline().strip()
        if line == "HELP":
            break
        numbers = list(map(int, line.split()))
        answer = sys.stdin.readline().strip()
        if answer == "YES":
            st.intersection_update(set(numbers))
        else:
            diff_st.update(set(numbers))
    st.difference_update(diff_st)
    print(*sorted(list(st)))


if __name__ == '__main__':
    main()
