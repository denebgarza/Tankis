import entity, camera

class Scene(object):
  def __init__(self, game, state = False):
    self.game = game
    self.state = state
    self.entities = []
    self.camera = camera.Camera(self, "Camera")

  def process(self):
    for entity in self.entities:
      # Calculate all screen coordinates for entities relative to the
      # scene's camera
      entity.screenX = entity.x - self.camera.x + self.game.WIDTH / 2;
      entity.screenY = entity.y - self.camera.y + self.game.HEIGHT / 2;
      entity.process()

  def render(self):
    for entity in self.entities:
      entity.render()

