from cell import Cell

class Board:
  def render_cells(self):
    self.cells = [[Cell() for column in range(3)] for row in range(3)]

  def render_board(self):
    cells = self.cells

    print(f"""
          _________________________________________________
          │               │               │               │
          │       {cells[0][2].translate_value()}       │       {cells[1][2].translate_value()}       │       {cells[2][2].translate_value()}       │
          _________________________________________________
          │               │               │               │
          │       {cells[0][1].translate_value()}       │       {cells[1][1].translate_value()}       │       {cells[2][1].translate_value()}       │
          _________________________________________________
          │               │               │               │
          │       {cells[0][0].translate_value()}       │       {cells[1][0].translate_value()}       │       {cells[2][0].translate_value()}       │
          │_______________│_______________│_______________│
        """)

b = Board()
b.render_cells()
b.render_board()

# '_________________________________________________'
# '│               │               │               │'
# '│       a       │       b       │       c       │'
# '│_______________│_______________│_______________│'
# '│               │               │               │'
# '│       d       │       e       │       f       │'
# '│_______________│_______________│_______________│'
# '│               │               │               │'
# '│       g       │       h       │       i       │'
# '│_______________│_______________│_______________│'
