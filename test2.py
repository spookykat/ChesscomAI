import ai
import chess

board = chess.Board()
AI = ai.Ai(board)

print(AI.Evaluate())