from dino_runner.utils.constants import (RUNNING, JUMPING, DUCKING)
import pygame

X_POS = 80
Y_POS = 255
Y_POS_DUCK = 370
JUMP_VEL = 8.5

RUN_1 = pygame.transform.scale(RUNNING[0], [200, 200])
RUN_2 = pygame.transform.scale(RUNNING[1], [200, 200])

class Dinosaur:
  def __init__(self):
    self.image = RUN_1
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = X_POS
    self.dino_rect.y = Y_POS
    self.step_index = 0
    self.jump_vel = JUMP_VEL
    self.dino_run = True
    self.dino_jump = False
    self.dino_duck = False
    
  def run(self):
    self.image = RUN_1 if self.step_index < 5 else RUN_2
    self.dino_rect.x = X_POS
    self.dino_rect.y = Y_POS
    self.step_index += 1  
    
  def jump(self):
    self.image = JUMPING
    if self.dino_jump:
      self.dino_rect.y -= self.jump_vel * 4
      self.jump_vel -= 0.6
    
    if self.jump_vel < -JUMP_VEL:
      self.dino_rect.y = Y_POS
      self.dino_jump = False
      self.jump_vel = JUMP_VEL

  def duck(self):
    self.image = pygame.transform.scale(DUCKING[0], [200, 200])
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = X_POS
    self.dino_rect.y = Y_POS_DUCK
    self.step_index += 1
    self.dino_duck = True

  def update(self, user_input):
    if self.dino_run:
      self.run()
    
    elif self.dino_jump:
      self.jump()
    
    elif self.dino_duck:
      self.duck()
      
    if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and not self.dino_jump:
      self.dino_jump = True
      self.dino_run = False
      self.dino_duck = False
      
    elif user_input[pygame.K_DOWN] and not self.dino_jump:
      self.dino_duck = True
      self.dino_run = False
      self.dino_jump = False
      
    elif not self.dino_jump:
      self.dino_run = True
      self.dino_jump = False
      self.dino_duck = False
      
      
    if self.step_index >= 10:
      self.step_index = 0
  
  def draw(self, screen):
    screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))