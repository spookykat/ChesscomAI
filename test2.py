import math
import ai
import chess

board = chess.Board("2kr4/ppp1qpb1/6pn/3b4/1n2Q3/4P3/PPPP2PP/RNB1KBNR w KQ - 13 15")

Ai1 = ai.Ai()
print(Ai1.minimax(4,-math.inf, math.inf, True,board))
print(Ai1.EvaluateScore(board))
print(board)