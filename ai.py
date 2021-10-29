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
          
                if self.board.turn == piece.color:
                    if piece.piece_type == 1 : #Pawn
                        evaluation += 1
                    elif piece.piece_type == 2 or piece.piece_type == 3 : #Bishop or knight
                        evaluation += 3
                    elif piece.piece_type == 4: #Rook
                        evaluation += 5
                    elif piece.piece_type == 5: #Queen
                        evaluation += 9

        return evaluation

