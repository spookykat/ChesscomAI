import pygame
import boardcom
import time
import os

class DrawBoard:
    def button(self, x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.screen, ac,(x,y,w,h))

            if click[0] == 1 and action != None:
                action()         
        else:
           pygame.draw.rect(self.screen, ic,(x,y,w,h))
        smallText = pygame.font.SysFont("comicsansms",20)
    def __init__(self, driver):
        pygame.init()
        self.screen = pygame.display.set_mode([560, 560])
        self.driver = driver
        self.board = boardcom.Boardcom() 
        pygame.draw.rect()
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
            self.drawBoard()
            self.button(20,20,50,50, (0,200,0), (0,255,0),self.drawBoard)
            pygame.display.flip()
        pygame.quit()

    def drawBoard(self):
        self.screen.fill((255,255,255))
        cnt = 0
        for y in range(8):
            for x in range(8):
                if cnt % 2 == 0:
                    pygame.draw.rect(self.screen, (255,255,255),pygame.Rect(x*70,y*70,70,70))
                else:
                    pygame.draw.rect(self.screen, (118, 150, 86),pygame.Rect(x*70,y*70,70,70))
                cnt +=1
            cnt -=1
        self.drawPieces(self.board.board)
    
    def drawPieces(self, board):
        list = []
        self.driver.GetBoard()
        self.board.pieceToBoard(self.driver.all_pieces)
        for i in range(8):
            for z in range(8):
                list.append([i,z])
        list.reverse()
        for i in range(64):
            if str(board.piece_at(i)).isupper():
                piece = str(board.piece_at(i)).lower()
                if piece == "p":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "white_pawn.png"))
                elif piece == "n":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "white_knight.png"))
                elif piece == "b":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "white_bishop.png"))
                elif piece == "r":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "white_rook.png"))
                elif piece == "q":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "white_queen.png"))
                elif piece == "k":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "white_king.png"))
                else: continue
            else:
                piece = str(board.piece_at(i)).lower()
                if piece == "p":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "black_pawn.png"))
                elif piece == "n":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "black_knight.png"))
                elif piece == "b":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "black_bishop.png"))
                elif piece == "r":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "black_rook.png"))
                elif piece == "q":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "black_queen.png"))
                elif piece == "k":
                    image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "pieces", "black_king.png"))
                else: continue
            self.screen.blit(pygame.transform.scale(image, (70,70)),((7-list[i][1])*70, (list[i][0])*70))