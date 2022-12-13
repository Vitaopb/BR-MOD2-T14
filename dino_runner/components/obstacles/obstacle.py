import pygame
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(pygame.sprite.Sprite):
  def __init__(self, image, _type):
    self.type = _type
    self.image = image
    self.rect = self.image[self.type].get_rect()
    self.rect.x = SCREEN_WIDTH
    
  def update(self, game_speed, obstacles):
    self.rect.x -= game_speed
    
    if self.rect.x < -self.rect.width:
      obstacles.pop()
    
  def draw(self, screen):
    screen.blit(self.image[self.type], (self.rect.x, self.rect.y))

  