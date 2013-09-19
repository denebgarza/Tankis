import pygame
import scene, entity, mainplayer

class Playable(scene.Scene):
  def __init__(self, game):
    super(Playable, self).__init__(game, True)

    self.map = []
    self.load_map()

    self.player = mainplayer.MainPlayer(
      self,
      "Tank",
      100,
      5 * 32, 5 * 32,
      32, 32,
      "tank.png"
    )
    
    self.entities.append(self.player)
    self.camera.x = self.game.WIDTH / 2
    self.camera.y = self.game.HEIGHT / 2
    self.camera.follow = self.player
    
  def load_map(self, path = None):
    if path is None:
      for i in xrange(0, 50):
        self.map.append([])
        for j in xrange(0, 50):
          tile = entity.Entity(self, "Tile", i * 32, j * 32, 32, 32, "tile.png")
          self.map[i].append(tile)
          self.entities.append(tile)
    pass

  def process(self):
    super(Playable, self).process()

    # process camera
    if self.camera.follow is not None:
      if self.camera.follow.x > self.game.WIDTH / 2 and self.camera.follow.x < len(self.map) * 32 - self.game.WIDTH / 2:
        self.camera.x = self.camera.follow.x
      if self.camera.follow.y > self.game.HEIGHT / 2 and self.camera.follow.y < len(self.map[0] * 32) - self.game.HEIGHT / 2:
        self.camera.y = self.camera.follow.y

    # process input
    if pygame.K_q in self.game.input:
      self.game.running = False
    
  def render(self):
    super(Playable, self).render()
