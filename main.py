from table import Game

game = Game()
game_over = False
while not game_over:
    if game.is_game_over() == 3:
        game_over = True
        print("It's a draw.")
        break
    game.make_move_x()
    if game.is_game_over() == 1:
        game_over = True
        print("X player wins!")
        break
    if game.is_game_over() == 3:
        game_over = True
        print("It's a draw.")
        break
    game.make_move_o()
    if game.is_game_over() == 2:
        game_over = True
        print("O player wins!")
        break
