
class TicTacToe:
    def __init__(self) -> None:
        self.player = 'X'
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]

    def display_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=' ')
            print()

    def play(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Wrong row or col")
        elif self.board[row][col] == '-':
            self.board[row][col] = self.player
            self.player = 'X' if self.player == 'O' else 'O'
        else:
            print("Error, position is occupied")

    def get_winner(self):
        # EXERCISE: Find the winner
        pass

    def is_tie():
        # EXERCISE: Find is is a Tie
        return False


game = TicTacToe()
while True:
    print(game.player, "plays")
    game.display_board()
    row = int(input("Row: "))
    col = int(input("Col: "))
    game.play(row, col)
    winner = game.get_winner()
    if winner is not None:
        print(winner, "wins")
        break
    if game.is_tie():
        print("Its a Tie")
        break
