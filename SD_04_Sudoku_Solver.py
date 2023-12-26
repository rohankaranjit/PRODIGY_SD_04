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
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def solve_sudoku(board):
    row, col = find_empty_location(board)

    if row == -1 and col == -1:
        return True  # Puzzle solved

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # If the puzzle is solved, return True

            board[row][col] = 0  # If not, backtrack

    return False

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if (j + 1) % 3 == 0 and j < 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print("-" * 21)
