import piececom
import chess

class Boardcom:
    def __init__(self, all_pieces):
        self.board = chess.Board()
        self.board.clear()
        for piece in all_pieces:
            self.pieceToBoard(piece)
    

    def pieceToBoard(self, compiece):
        square = chess.parse_square(compiece.position)
        piece = chess.Piece(compiece.pieceType, compiece.color)
        self.board.set_piece_at(square, piece)