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
                worth = 0

                if piece.piece_type == 1 : #Pawn
                    worth = 1
                elif piece.piece_type == 2 or piece.piece_type == 3 : #Bishop or knight
                    worth = 3
                elif piece.piece_type == 4: #Rook
                    worth = 5
                elif piece.piece_type == 5: #Queen
                    worth = 9


                if self.board.turn == piece.color:
                    evaluation += worth
                else:
                    evaluation -= worth

        return evaluation

