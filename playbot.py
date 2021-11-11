import chess
import math
from ai import Ai

board = chess.Board("3qk2r/p1rnb2p/5p2/1Q6/1p6/1P6/5PPP/2B2RK1 w k - 3 25")
Ai1 = Ai()

while True:
    move_bot = Ai1.minimax(4,-math.inf, math.inf, True, board)[0]
    board.push_uci(str(move_bot))
    print()
    print("Bot speelt " + str(move_bot))
    print(board)
    while True:
        print()
        print("Welke move? ")
        move_player = input()
        try:
            board.push_uci(move_player)
            break
        except:
            print("Move is illegaal")
            continue