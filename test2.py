import ai
import chess

board = chess.Board("rnbqkbnr/p1p3pp/p4p2/3pp3/4P3/7N/PPPP1PPP/RNBQK2R w KQkq - 0 5")

Ai1 = ai.Ai()
print(Ai1.minimax(3,True,board))
print(Ai1.EvaluateScore(board))
print(board)