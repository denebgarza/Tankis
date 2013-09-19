#Pygame imports
import pygame
from pygame.locals import *

class Game(object):
  def __init__(self, title = "My Game", width = 640, height = 480, windowed = True):
    self.running = True;
    self.screen = None
    self.TITLE = title;
    self.WIDTH = width
    self.HEIGHT = height
    self.WINDOWED = windowed
    self.scenes = []
    self.input = set()
    self.initialize()

  def initialize(self):
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    pygame.display.set_caption(self.TITLE)
    pygame.mouse.set_visible(0)
    pygame.init()

  def start(self):
    while self.running == True:
      self.process()
      self.render()

  def process(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          self.running = False
      elif event.type == pygame.KEYDOWN:
        if not pygame.key in self.input:
          self.input.add(event.key)
      elif event.type == pygame.KEYUP:
        self.input.discard(event.key)
      
    for scene in self.scenes:
      if(scene.state is not False):
        scene.process()
    pass

  def render(self):
    self.screen.fill((0, 0, 0))
    for scene in self.scenes:
      if(scene.state is not False):
        scene.render()
    pygame.display.flip()  

