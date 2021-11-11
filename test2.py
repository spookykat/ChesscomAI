import math
import ai
import chess
import piecesquaretables
import os

board = chess.Board("r5rk/5p1p/p1q1pPpQ/1p6/5R2/1P1B1b2/P1P4P/3R2K1 w - - 1 2")
Ai1 = ai.Ai()
print(Ai1.minimax(5,-math.inf, math.inf, True, board))
