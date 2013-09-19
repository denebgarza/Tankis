import entity

class Character(entity.Entity):
  def __init__(self, scene, name = "Character",
                     health = 100,
                     x = 0, y = 0, 
                     width = 0, height = 0, 
                     path = None):
    super(Character, self).__init__(scene, name, x, y, width, height, path)
    self.health = health
