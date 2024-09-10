import sys
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

# if you change CELL_COUNT, be sure that initial
# patterns in constructor are still valid
CELL_COUNT = 3
CELL_SIZE = 50
GRID_ORIGINX = 175
GRID_ORIGINY = 175
W_WIDTH = 500
W_HEIGHT = 500

class TicTacToe(QWidget):

  def __init__(self):
    super().__init__()
    self.setWindowTitle('TicTacToe')
    self.setGeometry(300, 300, W_WIDTH,W_HEIGHT)
    self.__turn = 0
    self.__winner = False
    self.__board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    self.show()


  def paintEvent(self, event):
    qp = QPainter()
    
    blackPen = QPen(QBrush(Qt.black), 1)  # Defining as variable to make it easier to reference
    
    qp.begin(self)
    
    # Clear the background
    qp.fillRect(event.rext(), Qt.white)
    
    qp.setPen(blackPen)
    
    for r in range(len(self.__board)):
        for c in range(len(self.__board[r])):
          qp.drawRect(GRID_ORIGINX + c * CELL_SIZE, GRID_ORIGINY + \
            r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    qp.end()

  def mousePressEvent(self, event):
    pass
    #figure out what cell they clicked in
    #retrieve that cell from the board



if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = TicTacToe()
  sys.exit(app.exec_())
