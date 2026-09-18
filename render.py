from game import chess_board, chess_positions, Converter
from moves_logic import Pawn

import pygame
pygame.init()
BOARD_SIZE = 8
SQUARE_SIZE = 80 
WIDTH = HEIGHT = BOARD_SIZE * SQUARE_SIZE
LIGHT_COLOR = (240, 217, 181)
DARK_COLOR = (181, 136, 99)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board")


images = {
    ".": pygame.transform.scale((pygame.image.load("chessPieces_photos/blank.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "p": pygame.transform.scale((pygame.image.load("chessPieces_photos/black-pawn.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "P": pygame.transform.scale((pygame.image.load("chessPieces_photos/white-pawn.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "q": pygame.transform.scale((pygame.image.load("chessPieces_photos/black-queen.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "Q": pygame.transform.scale((pygame.image.load("chessPieces_photos/white-queen.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "k": pygame.transform.scale((pygame.image.load("chessPieces_photos/black-king.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "K": pygame.transform.scale((pygame.image.load("chessPieces_photos/white-king.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "n": pygame.transform.scale((pygame.image.load("chessPieces_photos/black-knight.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "N": pygame.transform.scale((pygame.image.load("chessPieces_photos/white-knight.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "b": pygame.transform.scale((pygame.image.load("chessPieces_photos/black-bishop.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "B": pygame.transform.scale((pygame.image.load("chessPieces_photos/white-bishop.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "r": pygame.transform.scale((pygame.image.load("chessPieces_photos/black-rook.png")), (SQUARE_SIZE, SQUARE_SIZE)),
    "R": pygame.transform.scale((pygame.image.load("chessPieces_photos/white-rook.png")), (SQUARE_SIZE, SQUARE_SIZE)),
}
chess_squares = []
def Draw_Board(surface):
    for row, l, rows_pos in zip(range(BOARD_SIZE), chess_board, chess_positions):
        for col, p, pos in zip(range(BOARD_SIZE), l, rows_pos):
            color = LIGHT_COLOR if (row+col)%2==0 else DARK_COLOR
            image = images[p[0]]

            scaled_image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)


            if len(chess_board) <= 64:
                chess_squares.append([rect, pos])
            # print(chess_squares, "\n\n")
            pygame.draw.rect(surface, color, rect)
            screen.blit(scaled_image, rect)

moves = []
def handle_clicks(event):     
    global moves
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            for squares in chess_squares:
                if squares[0].collidepoint(event.pos):
                    moves.append(squares[1])
                    break

    if (len(moves) == 2):   
        if "p" in Converter.pos_to_name(moves[0]):
            black_pawn = Pawn(moves, "black")

        elif "P" in Converter.pos_to_name(moves[0]):
            white_pawn = Pawn(moves, "white")
        moves = []

    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            handle_clicks(event)
            
    Draw_Board(screen)
    
    pygame.display.flip()
pygame.quit()
