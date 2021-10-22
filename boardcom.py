import piececom
import chess

class Boardcom:
    def __init__(self, all_pieces):
        self.board = chess.Board()
        self.board.clear()
        for piece in all_pieces:
            self.pieceToBoard(piece)
    

    def pieceToBoard(self, piececom):
        square = chess.parse_square(piececom.position)
        piece = chess.Piece(piececom.pieceType, piececom.color)
        self.board.set_piece_at(square, piece)