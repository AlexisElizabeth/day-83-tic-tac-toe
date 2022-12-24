import time
from random import randint


class TicTacToe:

    def __init__(self):
        self.board = []
        self.space = " - "
        self.player = " X "
        self.computer = " 0 "

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

    def choose_symbol(self):
        player = input("Would you like to be X or O? > ").lower()
        if player == "x":
            self.player = " X "
            self.computer = " O "
        else:
            self.player = " O "
            self.computer = " X "

    def human_move(self):
        turn_ongoing = True
        while turn_ongoing:
            move = input("What is your move?  Enter in the format column, row (e.g. 1, 1) > ").split(", ")
            column_index = int(move[0]) - 1
            row_index = int(move[1]) - 1
            try:
                if self.board[row_index][column_index] == self.space:
                    self.board[row_index][column_index] = self.player
                    self.print_table()
                    self.search_for_win(self.player)
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
                self.board[random_row][random_column] = self.computer
                self.print_table()
                self.search_for_win(self.computer)
                turn_ongoing = False

    def search_for_win(self, active_player):
        # search for win in rows

        for row in self.board:
            win = True
            for character in row:
                if character != active_player:
                    win = False
                    break
            if win:
                return win

        # search for win in columns
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[j][i] != active_player:
                    win = False
                    break
            if win:
                return win

        # search for win in diagonal 1:
        win = True
        for k in range(3):
            if self.board[k][k] != active_player:
                win = False
                break
        if win:
            return win

        # search for win in diagonal 2:
        win = True
        for i in range(0, 3):
            if self.board[i][2 - i] != active_player:
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

    def start_game(self):
        self.build_table()
        self.print_table()
        self.choose_symbol()

    def player_order(self):
        print("Randomly picking a player to start the game")
        first = randint(1, 2)
        time.sleep(2)
        if first == 1:
            print("The human player starts")
            return self.player, self.computer
        else:
            print("The computer starts")
            return self.computer, self.player

    def game_ended(self, active_player):
        if self.search_for_win(active_player):
            print(f"{active_player} wins!")
            return True
        elif self.board_full():
            print("Board full!")
            return True
        return False

    def play_game(self):
        self.start_game()
        player_order = self.player_order()

        if player_order[0] == self.player:
            while not self.game_ended(self.player) or self.game_ended(self.computer):
                self.human_move()
                if self.game_ended(self.player):
                    break
                self.computer_move()
                if self.game_ended(self.computer):
                    break

        else:
            while not self.game_ended(self.player) or self.game_ended(self.computer):
                self.computer_move()
                if self.game_ended(self.computer):
                    break
                self.human_move()
                if self.game_ended(self.player):
                    break

        print("Game over!")

