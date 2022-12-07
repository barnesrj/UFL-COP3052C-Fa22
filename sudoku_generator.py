import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/
"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length
	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed
	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = self.get_board()
        self.box_length = int(pow(row_length, 0.5))

    '''
	Returns a 2D python list of numbers which represents the board
	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        height = self.row_length
        board = []
        row = []
        for i in range(1, height + 1):
            for j in range(9):
                temp = (i + j) % 9 + 1
                row.append(temp)

        for k in range(9):
            temp_row = []
            for l in range(9):
                temp_row.append(row[len(row) - 1])
                del row[len(row) - 1]
            board.append(temp_row)
        random.shuffle(board)

        temp_board = []
        for count in range(9):
            temp_board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        for x in range(9):
            for y in range(9):
                temp_board[x][y] = board[y][x]

        board = temp_board
        random.shuffle(board)


        board = self.remove_cells(board, self.removed_cells)
        return board




    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes
	Parameters: None
	Return: None
    '''

    def print_board(self):
        board = self.get_board()
        x = self.row_length
        for i in range(x):
            print(board[i])



    '''     
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True
	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        self.row = row
        self.num = num
        temp_row = []
        for i in range(self.row_length):
            temp_row.append(self.board[row][i])
        if num in temp_row:
            result = False
        else:
            result = True
        return result
    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True
	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        self.col = int(col)
        self.num = num
        temp_col = []
        for index in range(self.row_length):
            temp_col.append(self.board[index][int(col)])

        if num in temp_col:
            result = False
        else:
            result = True
        return result


    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True
	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box
	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        rows = 3
        cols = 3
        self.row_start = row_start
        self.col_start = int(col_start)
        self.num = num

        for i in range(rows):
            for j in range(cols):
                row = self.board[row_start + rows][int(col_start) + cols - 1]
                if num == row:
                    result = False
                    break
                else:
                    result = True
        return result


    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box
	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell
	Return: boolean
    '''

    def is_valid(self, row, col, num):
        self.row = row
        self.col = col
        self.num = num
        check1 = self.valid_in_row(row,num)
        check2 = self.valid_in_col(col,num)
        if row % 3 != 0:
            row_start = row // 3
        else:
            row_start = row
        if col %3 != 0:
            col_start = col // 3
        else:
            col_start = col
        check3 = self.valid_in_box(row_start, col_start, num)
        if check1== True and check2 == True and check3 == True:
            result = True
        else:
            result = False

        return result

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box
	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	Return: None
    '''

    def fill_box(self, row_start, col_start):
        nums = []
        i = self.row_length
        for num in range(i):
            nums.append(i + 1)

        for ind1 in range(3):
            for ind2 in range(3):
                x = (random.choice(nums))
                self.board[row_start+ind2][col_start + ind2] = x
                nums.pop(nums.index(x))




    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)
	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):

        num_boxes = self.row_length // 3
        for ind in range(num_boxes):
            self.fill_box(ind,ind)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell
	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][int(col)] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][int(col)] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining
	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again
	Parameters: None
	Return: None
    '''

    def remove_cells(self, board, remove_amount):
        l = self.row_length
        ht, wd, r = l, len(board[0]), []
        spaces = [[x, y] for x in range(ht) for y in range(wd)]
        for i in range(remove_amount):
            r = random.choice(spaces)
            board[r[0]][r[1]] = 0
            spaces.remove(r)
        return board


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution
Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)
Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    #sudoku.remove_cells()
    sudoku.print_board()
    sudoku.fill_values()
    board = sudoku.get_board()

    #board = sudoku.get_board()

    return board

def main():
    generate_sudoku(9,30)



if __name__ == "__main__":
    main()