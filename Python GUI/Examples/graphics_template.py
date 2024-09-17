import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint


class Face(QWidget):

  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 500, 500)
    self.setWindowTitle('Face')
    
    #Position of mouse clicks
    self.__x = -1
    self.__y = -1
    
    self.show() #Start the 

  #When an event happens (mouse click), draw the picture
  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    
    #Redraw the eye sockets
    qp.drawEllipse(100, 100, 100, 100)
    qp.drawEllipse(300, 100, 100, 100)
    
    #Draw Mouth
    qp.setPen(QPen(Qt.red, 8))
    qp.drawLine(150, 300, 250, 400)
    qp.drawLine(250, 400, 350, 300)
    
    #Draw the nose
    qp.setPen(QPen(Qt.blue, 1))
    qp.setBrush(Qt.blue)
    qp.drawPolygon(QPoint(250, 175), QPoint(200, 275), QPoint(300, 275))
    
    #Draw eyeballs
    qp.setPen(QPen(Qt.black, 5))
    qp.setBrush(Qt.black)
    if self.__x >= 0 and self.__y >= 0:
      xpercent = self.__x / 500
      ypercent = self.__y / 500
      
      qp.drawEllipse(int(100 + xpercent * 50), int(100 + ypercent * 50), 50, 50)
      qp.drawEllipse(int(300 + xpercent * 50), int(100 + ypercent * 50), 50, 50)
    else:
      qp.drawEllipse(125, 125, 50, 50)
      qp.drawEllipse(325, 125, 50, 50)  
    
    #Show coordinates of the clicks
    clicktext = 'No Clicks Yet'
    
    qp.end()

  def mousePressEvent(self, event):
    # pass #Placeholder for Python
    self.__x = event.x()
    self.__y = event.y()
    print(self.__x, self.__y)
    self.update()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Face()
  sys.exit(app.exec_())
