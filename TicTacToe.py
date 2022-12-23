import time
from random import randint


class TicTacToe:

    def __init__(self):
        self.board = []
        self.space = " - "
        self.x = " X "
        self.o = " 0 "

    def build_table(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.space)
            self.board.append(row)

    def print_table(self):
        for row in self.board:
            for space in row:
                print(space, end=" ")
            print()

    def human_move(self):
        turn_ongoing = True
        while turn_ongoing:
            move = input("What is your move?  Enter in the format column, row (e.g. 1, 1) > ").split(", ")
            column_index = int(move[0]) - 1
            row_index = int(move[1]) - 1
            try:
                if self.board[row_index][column_index] == self.space:
                    self.board[row_index][column_index] = self.x
                    self.print_table()
                    self.search_for_win(self.x)
                    turn_ongoing = False
                else:
                    print("That space is taken. Select again.")
            except IndexError:
                print("That space does not exist")

    def computer_move(self):
        print("Now the computer takes a turn.")
        time.sleep(2)
        turn_ongoing = True
        while turn_ongoing:
            random_row = randint(0, 2)
            random_column = randint(0, 2)
            if self.board[random_row][random_column] == self.space:
                self.board[random_row][random_column] = self.o
                self.print_table()
                self.search_for_win(self.o)
                turn_ongoing = False

    def search_for_win(self, player):
        # search for win in rows

        for row in self.board:
            win = True
            for character in row:
                if character != player:
                    win = False
                    break
            if win:
                return win

        # search for win in columns
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # search for win in diagonal 1:
        win = True
        for k in range(3):
            if self.board[k][k] != player:
                win = False
                break
        if win:
            return win

        # search for win in diagonal 2:
        win = True
        for i in range(0, 3):
            if self.board[i][2 - i] != player:
                win = False
                break
        if win:
            return win

    def board_full(self):
        full = True
        for row in self.board:
            for character in row:
                if character == self.space:
                    full = False
                    break
        return full
