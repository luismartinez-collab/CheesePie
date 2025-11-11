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

current_turn_white = True

selected_piece = None
selected_piece_type = None
selected_piece_color = None
selected_piece_starting_pos = None

selected_piece_pre_col = None
selected_piece_pre_row = None


def get_piece_at(row, col):
    for idx, piece in enumerate(pieces):
        if piece["row"] == row and piece["col"] == col:
            return idx, piece['type'], piece['color'], piece['startingPos']
    return None

def check_piece_in_the_way(piece_type, piece_color ,trying_to_move_to_row, trying_to_move_to_col, pre_move_row, pre_move_col):

    ##Finished pawn, 5 more

    if piece_type == "pawn":

        if piece_color == "white":

            for i in range(pre_move_row,trying_to_move_to_row-1,-1):

                if get_piece_at(i, pre_move_col) != None:

                    id_, piece, __, ___ = get_piece_at(i, pre_move_col)

                    if piece and id_ != selected_piece:

                        print(piece + " is in the way")

                        return False

                

        else:
            for i in range(pre_move_row,trying_to_move_to_row+1,1):

                if get_piece_at(i, pre_move_col) != None:

                    id_, piece, __, ___ = get_piece_at(i, pre_move_col)

                    if piece and id_ != selected_piece:

                        print(piece + " is in the way")

                        return False
                
               

                    
                
        return True

    elif piece_type == "bishop":

        return True

    elif piece_type == "rook":

        return True

    elif piece_type == "queen":

        return True

    elif piece_type == "king":
        
        return True
    

    return True


def check_move(piece_type, piece_color ,trying_to_move_to_row, trying_to_move_to_col, pre_move_row, pre_move_col, piece_starting_pos, whose_turn):

    if piece_color == "black" and whose_turn == True:
        return False
    elif piece_color == "white" and whose_turn == False:
        return False
    
    
    if piece_type == "pawn":
        
        if piece_color == "white":

            if (pre_move_row - 1 == trying_to_move_to_row and (pre_move_col + 1 or pre_move_col -1 == trying_to_move_to_col)):
                
                if get_piece_at(trying_to_move_to_row, trying_to_move_to_col):

                    id_, piece, color, __ = get_piece_at(trying_to_move_to_row, trying_to_move_to_col)

                    if color == "black" and pre_move_col != pieces[id_]["col"]:

                        pieces[id_]["row"] = -1

                        return True
                    else:
                        return False
                        
            valid = check_piece_in_the_way(piece_type, piece_color, trying_to_move_to_row, trying_to_move_to_col, pre_move_row, pre_move_col)
    
            if not valid:
                return False

            if trying_to_move_to_col != pre_move_col:
                return False
            
            if trying_to_move_to_row >= pre_move_row:
                return False
            
            if trying_to_move_to_row < pre_move_row - 1:
                if not piece_starting_pos:
                    return False
                else:
                    if trying_to_move_to_row < pre_move_row - 2:
                        return False
                    
            if trying_to_move_to_row == 0:
                pieces[selected_piece]["type"] == "queen"
                print("white queen")
            else:
                print("white pawn")
            

            return True

        else:

            if (pre_move_row + 1 == trying_to_move_to_row and (pre_move_col + 1 or pre_move_col -1 == trying_to_move_to_col)):
                
                if get_piece_at(trying_to_move_to_row, trying_to_move_to_col):

                    id_, piece, color, __ = get_piece_at(trying_to_move_to_row, trying_to_move_to_col)

                    if color == "white" and pre_move_col != pieces[id_]["col"]:
                        pieces[id_]["row"] = -1

                        return True

                        
            valid = check_piece_in_the_way(piece_type, piece_color, trying_to_move_to_row, trying_to_move_to_col, pre_move_row, pre_move_col)
    
            if not valid:
                return False

            if trying_to_move_to_col != pre_move_col:
                return False
            
            if trying_to_move_to_row <= pre_move_row:
                return False
            
            if trying_to_move_to_row > pre_move_row + 1:
                if not piece_starting_pos:
                    return False
                else:
                    if trying_to_move_to_row > pre_move_row + 2:
                        return False
                    
            if trying_to_move_to_row == 7:
                pieces[selected_piece]["type"] == "queen"
                print("black queen")
            else:
                print("black pawn")

            return True

    elif piece_type == "knight":

        valid_row = False
        valid_col = False

        if piece_color == "white":
            print("white knight")
        else:
            print("black knight")

        if (pre_move_row - 2 == trying_to_move_to_row) or (pre_move_row + 2 == trying_to_move_to_row):
            valid_row = True

            if (pre_move_col - 1 == trying_to_move_to_col) or (pre_move_col + 1 == trying_to_move_to_col):
                valid_col = True
        elif (pre_move_row - 1 == trying_to_move_to_row) or (pre_move_row + 1 == trying_to_move_to_row):
            valid_row = True

            if (pre_move_col - 2 == trying_to_move_to_col) or (pre_move_col + 2 == trying_to_move_to_col):
                valid_col = True
            

        if valid_col and valid_row:
            return True
        else:
            return False

    elif piece_type == "bishop":

        valor_absoluto_col = abs(trying_to_move_to_col - pre_move_col)
        valor_absoluto_row = abs(trying_to_move_to_row - pre_move_row)

        if valor_absoluto_col != valor_absoluto_row:
            return False
        
        if piece_color == "white":
            print("white bishop")
        else:
            print("black bishop")
        
        return True

    elif piece_type == "rook":

        valid_move = False

        if pre_move_col == trying_to_move_to_col:
            valid_move = True
        elif pre_move_row == trying_to_move_to_row:
            valid_move = True
        
        if piece_color == "white":
            print("white rook")
        else:
            print("black rook")

        if valid_move == True:
            return True
        else:
            return False
    elif piece_type == "queen":

        valid_move = False

        valor_absoluto_col = abs(trying_to_move_to_col - pre_move_col)
        valor_absoluto_row = abs(trying_to_move_to_row - pre_move_row)

        if pre_move_col == trying_to_move_to_col:
            valid_move = True
        elif pre_move_row == trying_to_move_to_row:
            valid_move = True
        elif valor_absoluto_col == valor_absoluto_row:
            valid_move = True
        
        if piece_color == "white":
            print("white queen")
        else:
            print("black queen")

        if valid_move == True:
            return True
        else:
            return False

    elif piece_type == "king":

        valid_move = False

        if (abs(trying_to_move_to_col - pre_move_col) == 1) and (abs(trying_to_move_to_row - pre_move_row) == 1):
            valid_move = True
        elif (abs(trying_to_move_to_col - pre_move_col) == 1) and (abs(trying_to_move_to_row - pre_move_row) == 0):
            valid_move = True
        elif (abs(trying_to_move_to_col - pre_move_col) == 0) and (abs(trying_to_move_to_row - pre_move_row) == 1):
            valid_move = True
        

        if piece_color == "white":
            print("white king")
        else:
            print("black king")

        if valid_move == True:
            return True
        else:
            return False



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
            starting_pos = None

            if get_piece_at(row, col) != None:
                idx, piece_type, piece_color, starting_pos = get_piece_at(row, col)
            
            if idx is not None or piece_type is not None:
                selected_piece = idx
                selected_piece_type = piece_type
                selected_piece_color = piece_color
                selected_piece_starting_pos = starting_pos

                selected_piece_pre_col = col
                selected_piece_pre_row = row
        elif event.type == pygame.MOUSEBUTTONUP:
            if (selected_piece is not None or piece_type is not None or piece_color is not None):
                mx, my = event.pos
                col, row = mx // SQUARE_SIZE, my // SQUARE_SIZE

                if check_move(selected_piece_type, selected_piece_color, row, col, selected_piece_pre_row, selected_piece_pre_col, selected_piece_starting_pos, current_turn_white):

                    print("After Move COL: " + str(col))
                    print("After Move ROW: " + str(row))

                    pieces[selected_piece]["startingPos"] = False
                    pieces[selected_piece]["row"] = row
                    pieces[selected_piece]["col"] = col


                    current_turn_white = not current_turn_white 
                    selected_piece = None
                    selected_piece_pre_row = None
                    selected_piece_pre_col = None
                    selected_piece_type = None
                    selected_piece_color = None
                    selected_piece_starting_pos = None
                else:
                    selected_piece = None
                    selected_piece_pre_row = None
                    selected_piece_pre_col = None
                    selected_piece_type = None
                    selected_piece_color = None
                    selected_piece_starting_pos = None

    draw_board(screen)
    draw_pieces(screen, pieces, images, selected_piece)
    pygame.display.flip()

pygame.quit()
sys.exit()