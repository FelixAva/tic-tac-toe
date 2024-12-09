class Cell:
  def __init__(self):
    self.state = None

  def set_state(self, new_state):
    self.state = new_state

  def translate_value(self):
    if self.state == 0:
      return 'O'

    return 'X'

cell = Cell()
cell.set_state(0)
cell.translate_value()
