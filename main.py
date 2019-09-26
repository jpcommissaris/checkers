import pygame
import time
from game_objects import Board

pygame.init()



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
            m = pygame.mouse.get_pos()
            if 265 < m[0] < 315 and 530 < m[1] < 555:
                b.doPass()
            b.pressed = True
            b.drawBoard(screen)
            b.drawPieces(screen)
            b.checkClick()

    if b.won():
        time.sleep(2)
        b.setBoard()




    # --- scene logic ---


    # --- repaints screen ---
    screen.fill((255,255,255))

    # --- new drawings ---
    b.drawBoard(screen)
    b.drawPieces(screen)


    # Updates screen with new drawings
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
