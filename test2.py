import ai
import chess
import math

board = chess.Board("rnb1k1nr/pppp1ppp/8/5q2/4p3/4b1P1/PPPPPP1P/RNBQKB1R w KQkq - 0 8")

Ai1 = ai.Ai()
print(Ai1.minimax(4,True,board,-math.inf,math.inf))

print(board)