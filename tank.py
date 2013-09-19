import entity, character

class Tank(character.Character):
  def __init__(self, scene, name = "Tank",
               health = 100, 
               x = 0, y = 0,
               width = 32, height = 32,
               path = None):
    super(Tank, self).__init__(scene, name, health, x, y, width, height, path)
    self.cannon = entity.Entity(scene, name.join("'s cannon"), x, y, width, height)
    