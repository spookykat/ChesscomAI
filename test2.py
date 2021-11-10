import math
import ai
import chess
import piecesquaretables

board = chess.Board("r1bqkbnr/ppp1pppp/2n5/3p4/8/2N2N2/PPPPPPPP/R1BQKB1R w KQkq - 2 3")
Ai1 = ai.Ai()
print(Ai1.minimax(3,-math.inf, math.inf, True,board)[0])
#testcommit