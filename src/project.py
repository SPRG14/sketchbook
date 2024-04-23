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


def draw_line(start, end, color, thickness):
  pygame.draw.line(canvas, color, start, end, thickness)


def handle_events():
  global drawing, last_pos, brush_size, brush_color


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      drawing = True
      last_pos = pygame.mouse.get_pos()
    elif event.type == pygame.MOUSEBUTTONUP:
      drawing = False
    elif event.type == pygame.MOUSEMOTION:
      if drawing:
        current_pos = pygame.mouse.get_pos()
        draw_line(last_pos, current_pos, brush_color, brush_size)
        last_pos = current_pos
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_c:
        canvas.fill(WHITE)


def main():
  global brush_size, brush_color


  while True:
    handle_events()


    screen.blit(canvas, (0, 0))


    pygame.display.flip()


if __name__ == "__main__":
  main()

