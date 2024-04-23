
class EightQueens:
    def __init__(self) -> None:
        self.board = [[0]*8 for i in range(8)]

    def is_attacked(self, row, col):
        # check if 1 exists in row
        # check if 1 exists in col
        # check if 1 exists in diagonals
        # if any 1 found return True
        # if does not exist return False
        return False
    
    def place_queen(self, row):
        # try to find a valid column
        if row == 8:
            # solution found, print it
            return    
        for col in range(8):
            if self.is_attacked(row, col):
                return
            else:
                self.board[row][col] = 1
                self.place_queen(row + 1)
                self.board[row][col] = 0
                




