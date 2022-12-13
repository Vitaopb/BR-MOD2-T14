from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
from dino_runner.components.dinosaur import Y_POS
import random

class Bird(Obstacle):
  def __init__(self):
    super().__init__(BIRD, 0)
    self.rect.y = Y_POS - random.randint(0, 70)
    self.step_index = 0
    
  def draw(self, screen):
    screen.blit(self.image[self.step_index // 5], self.rect)
    
    if  self.step_index >= 10:
      self.step_index = 0