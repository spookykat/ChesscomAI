import chess
import copy
import math

class Ai:
    def __init__(self):
        pass

    def GetMoves(self):
        return self.board.legal_moves

    def EvaluateScore(self, board):
        evaluation = 0
        cnt=0
        for square in chess.SQUARES:
            cnt += 1
            if board.piece_at(square) != None:
                piece = board.piece_at(square)
                worth = 0

                if piece.piece_type == 1 : #Pawn
                    worth = 1
                elif piece.piece_type == 2 or piece.piece_type == 3 : #Bishop or knight
                    worth = 3
                elif piece.piece_type == 4: #Rook
                    worth = 5
                elif piece.piece_type == 5: #Queen
                    worth = 9
                elif piece.piece_type == 6: #King
                    worth = 900


                if piece.color:
                    evaluation += worth
                else:
                    evaluation -= worth

        return evaluation

    def minimax(self, depth, player, board):
        board.turn = player
        children = list(board.legal_moves)
        best_move = None
        if depth == 0:
            return best_move, self.EvaluateScore(board)
        if player:
            max_eval = -math.inf
            for child in children:
                print(child)
                board_copy = copy.deepcopy(board)
                board_copy.push(child)
                current_eval = self.minimax(depth - 1, False, board_copy)[1]
                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move = child
            return best_move, max_eval
        
        else:
            min_eval = math.inf
            for child in children:
                print(child)
                board_copy = copy.deepcopy(board)
                board_copy.push(child)
                current_eval = self.minimax(depth - 1, True, board_copy)[1]
                if current_eval < min_eval:
                    min_eval = current_eval
                    best_move = child
            return best_move, min_eval
        
