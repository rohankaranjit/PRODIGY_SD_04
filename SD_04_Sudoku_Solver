def is_valid(board, row, col, num):
    # Check if the current row does not contain the same number
    if num in board[row]:
        return False

    # Check if the current column does not contain the same number
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the current 3x3 subgrid does not contain the same number
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True
