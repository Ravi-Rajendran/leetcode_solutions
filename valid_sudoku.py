'''
Validate Sudoku
https://leetcode.com/problems/valid-sudoku/description/
'''

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    def found_in_row_and_column(sudoku, check, num):
        row = check[0]
        col = check[1]
        for i in range(len(sudoku[0])):
            if sudoku[row][i] == num and i != check[1]:
                return True
            if sudoku[i][col] == num and i != check[0]:
                return True
        return False

    def found_in_grid(sudoku, row, col, check, num):
        for i in range(3):
            for j in range(3):
                if sudoku[i+row][j+col] == num and (i+row) != check[0] and (j+col) != check[1]:
                    return True
        return False

    def found(sudoku, check, num):
        return found_in_row_and_column(sudoku, check, num) or found_in_grid(sudoku, check[0] - check[0]%3, check[1] - check[1]%3, check, num)


    def validate_sudoku(board):
        for r, row in enumerate(board):
            for c, value in enumerate(row):
                if value != '.':
                    if found(board, [r, c], value):
                        return False
        return True

    return validate_sudoku(board)

def main():
    sudoku = [[".","8","7","6","5","4","3","2","1"],
              ["2",".",".",".",".",".",".",".","."],
              ["3",".",".",".",".",".",".",".","."],
              ["4",".",".",".",".",".",".",".","."],
              ["5",".",".",".",".",".",".",".","."],
              ["6",".",".",".",".",".",".",".","."],
              ["7",".",".",".",".",".",".",".","."],
              ["8",".",".",".",".",".",".",".","."],
              ["9",".",".",".",".",".",".",".","."]]

    for row in sudoku:
        print(row)
    print('=>', isValidSudoku(sudoku))

    sudoku = [[".","8","7","6","5","4","3","2","1"],
              ["2",".",".",".",".",".",".",".","."],
              ["3",".",".",".",".",".",".",".","."],
              ["4",".",".",".",".",".",".",".","."],
              ["5",".",".",".",".",".",".",".","."],
              ["6",".",".",".",".",".",".",".","."],
              ["7",".",".",".",".",".",".","2","."],
              ["8",".",".",".",".",".",".",".","."],
              ["9",".",".",".",".",".",".",".","."]]

    for row in sudoku:
        print(row)
    print('=>', isValidSudoku(sudoku))


if __name__ == '__main__':
    main()
