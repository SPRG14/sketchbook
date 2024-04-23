import pygame
import sys


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DEFAULT_BRUSH_SIZE = 5
DEFAULT_BRUSH_COLOR = BLACK


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Digital Drawing Pad")


canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
canvas.fill(WHITE)


drawing = False
last_pos = None
brush_size = DEFAULT_BRUSH_SIZE
brush_color = DEFAULT_BRUSH_COLOR

if __name__ == "__main__":
  main()

