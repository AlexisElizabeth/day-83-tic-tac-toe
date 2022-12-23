from TicTacToe import TicTacToe


if __name__ == "main":
    game = TicTacToe()
    game.build_table()
    game.print_table()

    while not game.board_full():
        while not game.search_for_win(game.x) or game.search_for_win(game.o):
            game.human_move()
            if game.search_for_win(game.x):
                print(f"{game.x} wins!")
                break
            game.computer_move()
            if game.search_for_win(game.o):
                print(f"{game.o} wins!")
                break

    print("Game over!")
