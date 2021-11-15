import tkinter as tk
from PIL import Image, ImageTk
from pieces import *

class boardGUI:

    size = 70
    
    green = "#769656"

    root = tk.Tk()


    canvas = tk.Canvas(root,height=560,width=670)
    canvas.pack()
    def __init__(self, board):
        self.board = board

    def drawCheckerboard(self):
        color = 'white'

        for y in range(8):

            for x in range(8):
                x1 = x * self.size
                y1 = y * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle((x1, y1, x2, y2), fill=color)
                if color == 'white':
                    color = self.green
                else:    
                    color = 'white'

            if color == 'white':
                color = self.green
            else:    
                color = 'white'



    def drawPiece(self, board):
        list = []
        for i in range(8):
            for z in range(8):
                list.append([i,z])
        list.reverse()
        for i in range(64):
            if str(board.piece_at(i)).isupper():
                piece = str(board.piece_at(i)).lower()
                if piece == "p":
                    self.img = ImageTk.PhotoImage(white_pawn)
                elif piece == "n":
                    self.img = ImageTk.PhotoImage(white_knight)
                elif piece == "b":
                    self.img = ImageTk.PhotoImage(white_bishop)
                elif piece == "r":
                    self.img = ImageTk.PhotoImage(white_rook)
                elif piece == "q":
                    self.img = ImageTk.PhotoImage(white_queen)
                elif piece == "k":
                    self.img = ImageTk.PhotoImage(white_king)
                else: continue
            else:
                piece = str(board.piece_at(i)).lower()
                if piece == "p":
                    self.img = ImageTk.PhotoImage(black_pawn)
                elif piece == "n":
                    self.img = ImageTk.PhotoImage(black_knight)
                elif piece == "b":
                    self.img = ImageTk.PhotoImage(black_bishop)
                elif piece == "r":
                    self.img = ImageTk.PhotoImage(black_rook)
                elif piece == "q":
                    self.img = ImageTk.PhotoImage(black_queen)
                elif piece == "k":
                    self.img = ImageTk.PhotoImage(black_king)
                else: continue
        
            self.canvas.create_image((70 * (7 -list[i][1])), 0, anchor=tk.NW,  image=self.img)

    def runDisplay(self):
        self.drawCheckerboard()
        self.drawPiece(self.board)
        self.root.mainloop()   