from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chess

class Chesscom:
    def __init__(self, driver):
        #change this to browser you are using
        #self.driver = webdriver.Chrome(os.path.join(os.path.dirname(os.path.realpath(__file__)),"chromedriver.exe"))
        self.driver = driver
        self.board = chess.Board()
        
    def pullBoard(self):
        self.board.clear()
        board = self.driver.find_element(By.CLASS_NAME,'board')

        all_pieces_raw = board.find_elements(By.CSS_SELECTOR,'*')
        all_pieces_classes = []
        self.all_pieces = []

        for test in all_pieces_raw:
            try:
                class_name = str(test.get_attribute("class"))
                if class_name.startswith("piece"):
                    all_pieces_classes.append(class_name)
            except:
                continue
               
        for piece in all_pieces_classes:

            piece_stripped = piece.strip('piece ')
            if piece_stripped.startswith("square"):
                color = piece_stripped[10:11] == "w"
                piecetypeString =  piece_stripped[11:12]
                position = chr(int(piece_stripped[7:8])+96) + piece_stripped[8:9]
            else:
                color = piece_stripped[:1] == "w"
                piecetypeString =  piece_stripped[1:2]
                position = chr(int(piece_stripped[10:11])+96) + piece_stripped[11:12]

            if piecetypeString == "p":
                pieceType = 1
            elif piecetypeString == "r":
                pieceType = 4
            elif piecetypeString == "n":
                pieceType = 2
            elif piecetypeString == "b":
                pieceType = 3
            elif piecetypeString == "q":
                pieceType = 5
            else:
                pieceType = 6
        
            

            self.board.set_piece_at(chess.parse_square(position),chess.Piece(pieceType, color))

    def printBoard(self):
        print(self.board)

    def getBoard(self):
        return self.board