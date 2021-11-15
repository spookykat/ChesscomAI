from PIL import Image, ImageTk
size = 70

white_pawn = Image.open('./pieces/white_pawn.png').resize((size, size))
white_knight = Image.open('./pieces/white_knight.png').resize((size, size))
white_bishop = Image.open('./pieces/white_bishop.png').resize((size, size))
white_rook = Image.open('./pieces/white_rook.png').resize((size, size))
white_queen = Image.open('./pieces/white_queen.png').resize((size, size))
white_king = Image.open('./pieces/white_king.png').resize((size, size))

black_pawn = Image.open('./pieces/black_pawn.png').resize((size, size))
black_knight = Image.open('./pieces/black_knight.png').resize((size, size))
black_bishop = Image.open('./pieces/black_bishop.png').resize((size, size))
black_rook = Image.open('./pieces/black_rook.png').resize((size, size))
black_queen = Image.open('./pieces/black_queen.png').resize((size, size))
black_king = Image.open('./pieces/black_king.png').resize((size, size))