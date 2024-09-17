''' 15-puzzle (sliding puzzle game) - JJ McCauley - Last Update 9/16/24'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import random as rand  # Shuffling board

'''Determine whether board is solvable
Parameters: The board list
Returns: Whether the board is not solvable (True)'''
def not_solvable(b):
    empty_index = b.index(0)
    
    #Calculating inversions
    inversions = 0
    for i in range(0, len(b)):
        for j in range(0, i):
            if b[j] > b[i]:
                inversions += 1
            
    # Returning Solvability
    if empty_index % 2 == 1 and inversions % 2 == 0:
        return False  # board is solvable
    elif empty_index % 2 == 0 and inversions % 2 == 1:
        return False  # board is solvable
    else:
        return True  # board is not solvable


'''Helper function that checks if the board is solved
Parameters: The board list
Returns: Whether the board was solved (True if solved, False if not)'''
def is_solved(b):
    return b == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


'''Makes the board, ensuring that it is solvable
Parameters: None
Returns: The solvable board as a 2-d list'''
def make_board():
    board = [num for num in range(0, 16)]  # 16 spots, 0-15
    rand.shuffle(board)  # Randomly generate spots
    while not_solvable(board):
        rand.shuffle(board)
    
    cols = 4
    n_board = [board[i:i+cols] for i in range(0, len(board), cols)]  # Convert 1d to 2d
    
    return n_board


''' GUI interface (PYQT5) & Intra-game Logic '''    
def main():

    # Getting the solvable board
    board = make_board()
    
    # Making a move counter to display on window
    m_counter = 0
    
    # Creating grid layouts
    top_grid = QGridLayout()  # Top grid for displaying moves made and instructions button
    grid = QGridLayout()
    
    # Creating master layout to store on root window
    root_layout = QVBoxLayout()
    root_layout.addLayout(top_grid)
    root_layout.addLayout(grid)
    
    # Configuring root window
    app = QApplication([])
    window = QWidget()
    icon = QIcon("15-puzzle-game-image.jpg")  # Custom icon for window
    window.setWindowIcon(icon)
    window.setWindowTitle("JJ's 15 Puzzle Game")
    window.setGeometry(100, 100, 800, 800) 
    
    # Add label displaying move count
    moves_label = QLabel(window)
    moves_label.setText(f"Moves Made: {m_counter}")
    moves_label.setFont(QFont("Arial", 16))
    top_grid.addWidget(moves_label)
    
    # Adding a button that displays a pop-up with instructions
    instructions_button = QPushButton("How to play")
    instructions_button.clicked.connect(on_help_button_click)
    top_grid.addWidget(instructions_button)
    
    # Adding numbers to grid
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                grid.addWidget(QPushButton(' '), i, j)
            else:
                grid.addWidget(QPushButton(f'{board[i][j]}'), i, j)
    
    # Show the window
    window.setLayout(root_layout)
    window.show()
    sys.exit(app.exec_())


'''Help Button Click Method - Displays directions for the game'''
def on_help_button_click():
    message = QMessageBox()
    message.setText("-Help Instructions Here-")
    message.setWindowTitle("15-Game Instructions")
    message.show()
    message.exec_()
   
# Good practice
if __name__ == '__main__':
    main()
    