from dino_runner.utils.constants import (
  FONT_SIZE, FONT_COLOR_BLACK, FONT_COLOR_WHITE, FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT
)
import pygame

def draw_message_component(
  message,
  screen,
  pos_y_center=SCREEN_HEIGHT / 2,
  pos_x_center=SCREEN_WIDTH / 2,
  font_size=FONT_SIZE,
  font_style=FONT_STYLE,
  font_color=FONT_COLOR_BLACK
):
  font = pygame.font.Font(font_style, font_size)
  text = font.render(f"{message}", True, font_color)
  text_rect = text.get_rect()
  text_rect.center = (pos_x_center, pos_y_center)
  screen.blit(text, text_rect)