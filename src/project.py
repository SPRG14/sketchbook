import pygame
import sys


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DEFAULT_BRUSH_SIZE = 5
DEFAULT_BRUSH_COLOR = BLACK
DEFAULT_BG = (255, 255, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SketchBook")


canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
canvas.fill(WHITE)


drawing = False
last_pos = None
brush_size = DEFAULT_BRUSH_SIZE
brush_color = DEFAULT_BRUSH_COLOR

font = pygame.font.Font(None, 36)


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
        canvas.fill(DEFAULT_BG)
      if event.key == pygame.K_1:
        brush_color = (0, 0, 0)
      if event.key == pygame.K_2:
        brush_color = (255, 255, 255)
      if event.key == pygame.K_3:
        brush_color = (255, 0, 0)
      if event.key == pygame.K_4:
        brush_color = (0, 255, 0)
      if event.key == pygame.K_5:
        brush_color = (0, 0, 255)
      if event.key == pygame.K_6:
        DEFAULT_BG = (255, 255, 255)
        canvas.fill(DEFAULT_BG)
      if event.key == pygame.K_7:
        DEFAULT_BG = (0, 0, 0)
        canvas.fill(DEFAULT_BG)
      if event.key == pygame.K_8:
        DEFAULT_BG = (255, 0, 0)
        canvas.fill(DEFAULT_BG)
      if event.key == pygame.K_9:
        DEFAULT_BG = (0, 255, 0)
        canvas.fill(DEFAULT_BG)
      if event.key == pygame.K_0:
        DEFAULT_BG = (0, 0, 255)
        canvas.fill(DEFAULT_BG)

def display_details():
  1

def main():
  global brush_size, brush_color


  while True:
    handle_events()
    

    screen.blit(canvas, (0, 0))
    pygame.draw.rect(screen, brush_color, (0, 0, SCREEN_WIDTH - 0, SCREEN_HEIGHT - 0), 40)

    pygame.display.flip()


if __name__ == "__main__":
  main()

