# ---------------------------
# Import of modules
# ---- -----------------------

import pygame
from pygame.locals import *
import sys

# -----------
# Constants
# -----------

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


# ------------------------------
# Classes and Functions used
# ------------- -----------------


# ------------------------------
# Main function of the game
# ------------- -----------------


def main():
    pygame.init()
    # create the window and give it a title:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("pygame tutorial part 2")

    # load the background and an image ("Surface" objects are created)
    background = pygame.image.load("background.jpg").convert()
    tux = pygame.image.load("tux.png").convert_alpha()

    tux_pos_x = 550
    tux_pos_y = 200

    # We indicate the position of the "Surface" on the screen
    screen.blit(tux, (tux_pos_x, tux_pos_y))
    screen.blit(background, (0, 0))
    # the changes are shown on the screen
    pygame.display.flip()

    # the main loop of the game
    while True:
        # we subtract 1 from the x coordinate of tux and check
        # that it does not reach the edge of the screen
        tux_pos_x = tux_pos_x - 1
        if tux_pos_x < 1:
            tux_pos_x = 550

        # Redraw all the elements of the screen
        screen.blit(background, (0, 0))
        screen.blit(tux, (tux_pos_x, tux_pos_y))
        # the changes are shown on the screen
        pygame.display.flip()

        # Possible keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
