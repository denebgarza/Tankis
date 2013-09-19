import pygame, os
from pygame.locals import *

class Entity(object):
  def __init__(self, scene, name = "Entity",
                     x = 0, y = 0, 
                     width = 0, height = 0, 
                     image_path = None):
    self.scene = scene
    self.surface = None
    self.screenX = x;
    self.screenY = y;
    self.x = x;
    self.y = y;
    self.load_image(image_path)
  
  def load_image(self, image_path, colorkey = None):
    if image_path is not None:
      image_path = os.path.join('assets', image_path)
      try:
        self.surface = pygame.image.load(image_path)
      except pygame.error, message:
        print 'Cannot load pygame.surface:', image_path
        raise SystemExit, message
      self.surface = self.surface.convert()
      if colorkey is None:
        colorkey = self.surface.get_at((0, 0))
      self.surface.set_colorkey(colorkey)
    
  def render(self):
    if self.surface is not None:
      self.scene.game.screen.blit(self.surface, (self.screenX, self.screenY))

  def process(self):
    pass

  def rotate(self, angle):
      oldRect = self.surface.get_rect()

      # rotate (rotozoom because of antialias)
      rotImage = pygame.transform.rotozoom(self.surface, angle, 1)

      # get rect of rotated surface and set its center to the old center
      rotRect = rotImage.get_rect()
      rotRect.center = oldRect.center
      
      self.surface = rotImage
      return rotImage, rotRect