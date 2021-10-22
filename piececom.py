class PieceCom:
    def __init__(self, piece):
        self.piece = piece
        self.GetPieceInfo()
        

    def GetPieceInfo(self):
        piece_stripped = self.piece.strip('piece ')

        self.color = piece_stripped[:1] == "w"

        if piece_stripped[1:2] == "p":
            self.pieceType = 1
        elif piece_stripped[1:2] == "r":
            self.pieceType = 4
        elif piece_stripped[1:2] == "n":
            self.pieceType = 2
        elif piece_stripped[1:2] == "b":
            self.pieceType = 3
        elif piece_stripped[1:2] == "q":
            self.pieceType = 5
        else:
            self.pieceType = 6
        
        self.position = chr(int(piece_stripped[10:11])+96) + piece_stripped[11:12]