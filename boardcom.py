import piececom
import chess

class Boardcom:
    def __init__(self):
        self.board = chess.Board()
        
    
    def pieceToBoard(self, all_pieces):
        self.board.clear()  
        for piece in all_pieces:
            square = chess.parse_square(piece.position)
            piece = chess.Piece(piece.pieceType, piece.color)
            self.board.set_piece_at(square, piece)