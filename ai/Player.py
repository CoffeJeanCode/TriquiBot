class Player:
  def __init__(self, sign, name):
    self.sign = sign
    self.score = 0
    self.name = name
  
  def __str__(self):
    return f"{self.name} {self.sign.upper()}"