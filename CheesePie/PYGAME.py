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
pygame.display.set_caption("Movable Chess Pieces")

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
    {"row": 0, "col": 0, "color": "black", "type": "rook"},
    {"row": 0, "col": 1, "color": "black", "type": "knight"},
    {"row": 0, "col": 2, "color": "black", "type": "bishop"},
    {"row": 0, "col": 3, "color": "black", "type": "queen"},
    {"row": 0, "col": 4, "color": "black", "type": "king"},
    {"row": 0, "col": 5, "color": "black", "type": "bishop"},
    {"row": 0, "col": 6, "color": "black", "type": "knight"},
    {"row": 0, "col": 7, "color": "black", "type": "rook"}
] + [
    {"row": 1, "col": col, "color": "black", "type": "pawn"} for col in range(8)
] + [
    {"row": 7, "col": 0, "color": "white", "type": "rook"},
    {"row": 7, "col": 1, "color": "white", "type": "knight"},
    {"row": 7, "col": 2, "color": "white", "type": "bishop"},
    {"row": 7, "col": 3, "color": "white", "type": "queen"},
    {"row": 7, "col": 4, "color": "white", "type": "king"},
    {"row": 7, "col": 5, "color": "white", "type": "bishop"},
    {"row": 7, "col": 6, "color": "white", "type": "knight"},
    {"row": 7, "col": 7, "color": "white", "type": "rook"}
] + [
    {"row": 6, "col": col, "color": "white", "type": "pawn"} for col in range(8)
]

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
            return idx
    return None

selected_piece = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            col, row = mx // SQUARE_SIZE, my // SQUARE_SIZE
            idx = get_piece_at(row, col)
            if idx is not None:
                selected_piece = idx
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_piece is not None:
                mx, my = event.pos
                col, row = mx // SQUARE_SIZE, my // SQUARE_SIZE
                pieces[selected_piece]["row"] = row
                pieces[selected_piece]["col"] = col
                selected_piece = None

    draw_board(screen)
    draw_pieces(screen, pieces, images, selected_piece)
    pygame.display.flip()

pygame.quit()
sys.exit()