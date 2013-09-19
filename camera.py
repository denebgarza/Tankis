import entity

class Camera(entity.Entity):
  def __init__(self, scene, name = "Camera",
                     x = 0, y = 0, 
                     width = 0, height = 0, 
                     path = None):
    super(Camera, self).__init__(scene, name, x, y, width, height, path)
    self.follow = None
    self.effects = []
    
