import chess
import copy
import math
from piecesquaretables import *


class Ai:
    def __init__(self):
        pass

    def EvaluateScore(self, board):
        evaluation = 0
        if board.is_checkmate():
            if board.turn:
                evaluation += -math.inf
            else:
                evaluation += math.inf
        
        for square in chess.SQUARES:
            if board.piece_at(square) != None:
                piece = board.piece_at(square)
                
                if piece.color:
                    piece_table = piece_table_white
                else: 
                    piece_table = piece_table_black
                #Material
                worth = 0              
                if piece.piece_type == 1 : #Pawn
                    worth = 100
                    worth += piece_table[0][square]
                elif piece.piece_type == 2 : #Knight
                    worth = 300
                    worth += piece_table[1][square]
                elif piece.piece_type == 3: #Bishop
                    worth = 320
                elif piece.piece_type == 4: #Rook
                    worth = 500
                elif piece.piece_type == 5: #Queen
                    worth = 900


                if piece.color:
                    evaluation += worth
                else:
                    evaluation -= worth
                
        return evaluation

    def minimax(self, depth, alpha, beta, player, board):
        board.turn = player
        children = list(board.legal_moves)
        best_move = None
        if depth == 0:
            return best_move, self.EvaluateScore(board)
        if player:
            max_eval = -math.inf
            for child in children:
                board_copy = copy.deepcopy(board)
                board_copy.push(child)
                current_eval = self.minimax(depth - 1, alpha, beta, False, board_copy)[1]
                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move = child
                alpha = max(alpha, current_eval)
                if beta <= alpha:
                    break
            return best_move, max_eval
        
        else:
            min_eval = math.inf
            for child in children:
                board_copy = copy.deepcopy(board)
                board_copy.push(child)
                current_eval = self.minimax(depth - 1,alpha, beta, True, board_copy)[1]
                if current_eval < min_eval:
                    min_eval = current_eval
                    best_move = child
                beta = min(beta,current_eval)
                if beta <= alpha:
                    break
            return best_move, min_eval
        
