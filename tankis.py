import game, scene, entity, playable

class Tankis(game.Game):
  def __init__(self, width, height):
    super(Tankis, self).__init__("Tankis", width, height)
    self.scenes.append(playable.Playable(self))

  def initialize(self):
    super(Tankis, self).initialize()

  def process(self):
    super(Tankis, self).process()

  def render(self):
    super(Tankis, self).render()