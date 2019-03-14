import pygame
from checkers.board import Board

pygame.init()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the screen [width, height]
length = 600
width = 600
size = (length, width)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

scene=1

def scene1():
    global scene
    scene = 2
    b.setBoard()
    pass

def scene2():
    global scene
    pass

b = Board()
b.setBoard()



# --- game loop ---
while not done:
    b.pressed = False
    # --- Events loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            b.checkClick(screen)

    # --- scene logic ---


    # --- repaints screen ---
    screen.fill(WHITE)

    # --- new drawings ---
    b.drawBoard(screen)
    b.drawPieces(screen)


    # Updates screen with new drawings
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
