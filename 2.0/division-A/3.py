def main():
    board = [list(map(int, input().split())) for _ in range(3)]
    transposed_board = [[board[j][i] for j in range(3)] for i in range(3)]
    linear_board = []
    for row in board:
        linear_board.extend(row)
    one_count = linear_board.count(1)
    two_count = linear_board.count(2)
    zero_count = linear_board.count(0)
    if one_count - two_count != 1 and one_count - two_count != 0:
        print("NO")
        return
    if not zero_count:
        if two_count != 4 or one_count != 5:
            print("NO")
            return
    one_wins = 0
    two_wins = 0
    for row in board:
        if row.count(1) == 3:
            one_wins += 1
        elif row.count(2) == 3:
            two_wins += 1
    for row in transposed_board:
        if row.count(1) == 3:
            one_wins += 1
        elif row.count(2) == 3:
            two_wins += 1
    if board[0][0] == board[1][1] == board[2][2] == 1:
        one_wins += 1
    if board[0][0] == board[1][1] == board[2][2] == 2:
        two_wins += 1
    if board[0][2] == board[1][1] == board[2][0] == 1:
        one_wins += 1
    if board[0][2] == board[1][1] == board[2][0] == 2:
        two_wins += 1
    if one_wins and two_wins:
        print("NO")
        return
    if one_wins > 2 or two_wins > 2:
        print("NO")
        return
    if one_wins:
        if one_count - 1 != two_count:
            print("NO")
            return
        print("YES")
        return
    if two_wins:
        if one_count != two_count:
            print("NO")
            return
        print("YES")
        return

    print("YES")


if __name__ == '__main__':
    main()
