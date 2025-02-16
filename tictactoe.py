class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def print_board_nums(self):
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player="X", o_player="O", print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"  # starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == "X":
            square = int(input(f"{x_player}'s turn. Input move (0-8): "))
        else:
            square = int(input(f"{o_player}'s turn. Input move (0-8): "))

        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print("")  # empty line

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            # alternate letters after successful move
            letter = "O" if letter == "X" else "X"

        else:
            print("Invalid move. Try again.")

    if print_game:
        print("It's a tie!")

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    print("Board positions are numbered from 0-8 as shown below:")
    t = TicTacToe()
    play(t)
