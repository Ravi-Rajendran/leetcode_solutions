'''
Sudoku Solver
https://leetcode.com/problems/sudoku-solver/description/
'''

def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    def find_free_space(board, free):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    free[0], free[1] = row, col
                    return True
        return False

    def valid_row(board, row, num):
        for col in range(len(board[0])):
            if board[row][col] == num:
                return False
        return True

    def valid_column(board, col, num):
        for row in range(len(board)):
            if board[row][col] == num:
                return False
        return True

    def valid_box(board, row, col, num):
        for i in range(3):
            for j in range(3):
                if board[i+row][j+col] == num:
                    return False
        return True

    def is_safe(board, free, num):
        return valid_row(board, free[0], num) and valid_column(board, free[1], num) and valid_box(board, free[0]-free[0]%3, free[1]-free[1]%3, num)

    def solver(board):
        free = [0, 0]
        if not find_free_space(board, free):
            return True
        for num in range(1, len(board)+1):
            if is_safe(board, free, str(num)):
                board[free[0]][free[1]] = str(num)
                if solver(board):
                    return True
                board[free[0]][free[1]] = '.'
        return False

    solver(board)

board = [[".",".","9","7","4","8",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]

solveSudoku(board)

for row in board:
    print(row)
