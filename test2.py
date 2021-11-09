import math
import ai
import chess

board = chess.Board()
board.turn = True
Ai1 = ai.Ai()
print(Ai1.minimax(4,-math.inf, math.inf, True,board))