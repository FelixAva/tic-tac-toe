class Cell:
  def __init__(self):
    self.state = None

  def set_state(self, new_state):
    self.state = new_state

  def translate_value(self):
    if self.state == None:
      return ' '
    elif self.state == 0:
      return 'O'

    return 'X'
