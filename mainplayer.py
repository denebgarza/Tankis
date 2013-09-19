import pygame
import tank

class MainPlayer(tank.Tank):
  def __init__(self, scene, name = "Main Player", health = 100,
                     x = 0, y = 0,
                     width = 0, height = 0,
                     path = None):
    super(MainPlayer, self).__init__(scene, name, health, x, y, width, height, path)

  def process(self):
    self.input = self.scene.game.input
    if pygame.K_a in self.input:
      self.x -= 3
    if pygame.K_d in self.input:
      self.x += 3
    if pygame.K_w in self.input:
      self.y -= 3
    if pygame.K_s in self.input:
      self.y += 3
    if pygame.K_r in self.input:
      self.rotate(5)