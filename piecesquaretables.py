
pawn_white_table = [
    0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0, 25, 25,  0,  0,  0,
    0,  0,  0, 20, 20,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,-20,-20, 0, 0,  0,
    0,  0,  0,  0,  0,  0,  0,  0
]
knight_white_table = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50,
]

pawn_black_table = pawn_white_table[::-1]
knight_black_table = knight_white_table[::-1]


piece_table_white = [pawn_white_table, knight_white_table]
piece_table_black = [pawn_black_table, knight_black_table]