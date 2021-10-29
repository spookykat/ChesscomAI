import ai
import chess

board = chess.Board("rnb1k1nr/pppp1ppp/8/2b2q2/4p1N1/6P1/PPPPPP1P/RNBQKB1R w KQkq - 8 7")

Ai1 = ai.Ai()
print(Ai1.minimax(4,True,board))

print(board)