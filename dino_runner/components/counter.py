import pygame

fira_code = pygame.font.match_font('fira code')
print(fira_code)

class Counter:
  def __init__(self):
    self.score = 000000
        
  def update(self):
    self.score += 1
    
  def draw(self, screen):
    font = pygame.font.Font(fira_code, 30)
    text = font.render(str(self.score), True, (0, 0, 0))
    screen.blit(text, (1050, 10))