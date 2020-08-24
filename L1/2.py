# ---------------------------
# Import of modules
# ---------------- -----------

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

    # the main game loop
    while True:
        # Possible keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
