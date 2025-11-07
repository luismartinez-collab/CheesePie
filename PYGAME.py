import pygame
import sys
import os

pygame.init()

WIDTH, HEIGHT = 480, 480
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WHITE = (245, 245, 220)
BLACK = (139, 69, 19)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CheesePie")

def draw_board(screen):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

def load_piece_images(base_folder="Imagenes"):
    piece_types = ["king", "queen", "rook", "bishop", "knight", "pawn"]
    colors = ["black", "white"]
    images = {}
    for color in colors:
        for ptype in piece_types:
            folder = "BlackPieces" if color == "black" else "WhitePieces"
            filename = str(f"{color}-{ptype}.png")
            path = os.path.join(base_folder, folder, filename)
            img = pygame.image.load(path)
            img = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))
            images[f"{color}-{ptype}"] = img
    return images

images = load_piece_images()

# Example starting positions (expand for all pieces)
pieces = [
    {"row": 0, "col": 0, "color": "black", "type": "rook", "startingPos": True},
    {"row": 0, "col": 1, "color": "black", "type": "knight", "startingPos": True},
    {"row": 0, "col": 2, "color": "black", "type": "bishop", "startingPos": True},
    {"row": 0, "col": 3, "color": "black", "type": "queen", "startingPos": True},
    {"row": 0, "col": 4, "color": "black", "type": "king", "startingPos": True},
    {"row": 0, "col": 5, "color": "black", "type": "bishop", "startingPos": True},
    {"row": 0, "col": 6, "color": "black", "type": "knight", "startingPos": True},
    {"row": 0, "col": 7, "color": "black", "type": "rook", "startingPos": True}
] + [
    {"row": 1, "col": col, "color": "black", "type": "pawn", "startingPos": True} for col in range(8)
] + [
    {"row": 7, "col": 0, "color": "white", "type": "rook", "startingPos": True},
    {"row": 7, "col": 1, "color": "white", "type": "knight", "startingPos": True},
    {"row": 7, "col": 2, "color": "white", "type": "bishop", "startingPos": True},
    {"row": 7, "col": 3, "color": "white", "type": "queen", "startingPos": True},
    {"row": 7, "col": 4, "color": "white", "type": "king", "startingPos": True},
    {"row": 7, "col": 5, "color": "white", "type": "bishop", "startingPos": True},
    {"row": 7, "col": 6, "color": "white", "type": "knight", "startingPos": True},
    {"row": 7, "col": 7, "color": "white", "type": "rook", "startingPos": True}
] + [
    {"row": 6, "col": col, "color": "white", "type": "pawn", "startingPos": True} for col in range(8)
]

def check_move(piece_type, piece_color ,trying_to_move_to_row, trying_to_move_to_col, pre_move_row, pre_move_col):
    
    if piece_type == "pawn":
        
        if piece_color == "white":

            if trying_to_move_to_col != pre_move_col:
                return False
            
            if trying_to_move_to_row >= pre_move_row:
                return False
            
            print("white pawn")

            return True


        else:

            if trying_to_move_to_col != pre_move_col:
                return False
            
            if trying_to_move_to_row <= pre_move_row:
                return False
            
            print("black pawn")

            return True

    elif piece_type == "knight":

        valid_row = False
        valid_col = False

        if piece_color == "white":
            print("white knight")
        else:
            print("black knight")

        ##First i check the rows 
        if (pre_move_row - 1 == trying_to_move_to_row) or (pre_move_row - 2 == trying_to_move_to_row) or (pre_move_row + 1 == trying_to_move_to_row) or (pre_move_row + 2 == trying_to_move_to_row):
            valid_row = True


        ##Then i check the columns for the L patern 
        if (pre_move_col - 1 == trying_to_move_to_col) or (pre_move_col - 2 == trying_to_move_to_col) or (pre_move_col + 1 == trying_to_move_to_col) or (pre_move_col + 2 == trying_to_move_to_col):
            if trying_to_move_to_row ##fix

        if valid_col and valid_row:
            return True
        else:
            return False

    elif piece_type == "bishop":
        
        if piece_color == "white":
            print("white bishop")
        else:
            print("black bishop")

    elif piece_type == "rook":
        
        if piece_color == "white":
            print("white rook")
        else:
            print("black rook")

    elif piece_type == "queen":
        
        if piece_color == "white":
            print("white queen")
        else:
            print("black queen")

    elif piece_type == "king":

        if piece_color == "white":
            print("white king")
        else:
            print("black king")

    return True


def draw_pieces(screen, pieces, images, selected=None):
    for idx, piece in enumerate(pieces):
        if idx == selected:
            continue
        x = piece["col"] * SQUARE_SIZE
        y = piece["row"] * SQUARE_SIZE
        image_key = f"{piece['color']}-{piece['type']}"
        image = images[image_key]
        screen.blit(image, (x, y))
    # Draw selected piece at mouse position
    if selected is not None:
        mx, my = pygame.mouse.get_pos()
        image_key = f"{pieces[selected]['color']}-{pieces[selected]['type']}"
        image = images[image_key]
        screen.blit(image, (mx - SQUARE_SIZE // 2, my - SQUARE_SIZE // 2))

def get_piece_at(row, col):
    for idx, piece in enumerate(pieces):
        if piece["row"] == row and piece["col"] == col:
            return idx, piece['type'], piece['color']
    return None

selected_piece = None
selected_piece_type = None
selected_piece_color = None

selected_piece_pre_col = None
selected_piece_pre_row = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            col, row = mx // SQUARE_SIZE, my // SQUARE_SIZE
            print("Pre Move COL: " + str(col))
            print("Pre Move ROW: " + str(row))

            idx = None
            piece_type = None
            piece_color = None

            if get_piece_at(row, col) != None:
                idx, piece_type, piece_color = get_piece_at(row, col)
            
            if idx is not None or piece_type is not None:
                selected_piece = idx
                selected_piece_type = piece_type
                selected_piece_color = piece_color

                selected_piece_pre_col = col
                selected_piece_pre_row = row
        elif event.type == pygame.MOUSEBUTTONUP:
            if (selected_piece is not None or piece_type is not None or piece_color is not None):
                mx, my = event.pos
                col, row = mx // SQUARE_SIZE, my // SQUARE_SIZE

                print("After Move COL: " + str(col))
                print("After Move ROW: " + str(row))
                print("Selected Piece: " + str(selected_piece))
                print("Selected Piece Type: " + str(selected_piece_type))
                print("Selected Piece Color: " + str(selected_piece_color))

                if check_move(selected_piece_type, selected_piece_color, row, col, selected_piece_pre_row, selected_piece_pre_col):

                    pieces[selected_piece]["row"] = row
                    pieces[selected_piece]["col"] = col

                    selected_piece = None
                    selected_piece_pre_row = None
                    selected_piece_pre_col = None
                    selected_piece_type = None
                    selected_piece_color = None
                else:
                    selected_piece = None
                    selected_piece_pre_row = None
                    selected_piece_pre_col = None
                    selected_piece_type = None
                    selected_piece_color = None

    draw_board(screen)
    draw_pieces(screen, pieces, images, selected_piece)
    pygame.display.flip()

pygame.quit()
sys.exit()