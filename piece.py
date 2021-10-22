class Piece:
    def __init__(self, piece):
        self.piece = piece
        self.GetPieceInfo()
        

    def GetPieceInfo(self):
        piece_stripped = self.piece.strip('piece ')

        self.color = "white" if piece_stripped[:1] == "w" else "black"

        if piece_stripped[1:2] == "p":
            self.pieceType = "pawn"
        elif piece_stripped[1:2] == "r":
            self.pieceType = "rook"
        elif piece_stripped[1:2] == "n":
            self.pieceType = "knight"
        elif piece_stripped[1:2] == "b":
            self.pieceType = "bishop"
        elif piece_stripped[1:2] == "q":
            self.pieceType = "queen"
        else:
            self.pieceType = "king"
        
        self.position = chr(int(piece_stripped[10:11])+96) + piece_stripped[11:12]