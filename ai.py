import chess
class Ai:
    def __init__(self, board):
        self.board = board

    def GetMoves(self):
        return self.board.legal_moves

    def Evaluate(self):
        evaluation = 0
        cnt=0
        for square in chess.SQUARES:
            cnt += 1
            if self.board.piece_at(square) != None:
                piece = self.board.piece_at(square)
          
                if piece.color:
                    evaluation += 20

        return evaluation

