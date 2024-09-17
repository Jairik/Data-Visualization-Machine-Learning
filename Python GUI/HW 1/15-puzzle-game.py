''' 15-puzzle (sliding puzzle game) - JJ McCauley - Last Update 9/16/24'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
import random as rand  # Shuffling board

# Global Constants
BOARD_SIZE = 4

'''Determine whether board is solvable
Parameters: The board list
Returns: Whether the board is not solvable (True)'''
def not_solvable(b):
    empty_index = b.index(0)
    
    #Calculating inversions
    inversions = 0
    for i in range(0, BOARD_SIZE):
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

'''Helper function that returns the index of a given number
Parameters: The board list, value to find
Returns: A pair (row, col)'''
def find_num(board, val):
    for i, row in enumerate(board):
        if val in row:
            j = row.index(val)
            return i, j
    return None  # Should never happen

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
    window.setStyleSheet("background-color: #1c1c1c; color: white; font-family: Tahoma; font-size: 18px;")
    
    # Add label displaying move count
    moves_label = QLabel()
    moves_label.setText(f"Moves Made: {m_counter}")
    moves_label.setFont(QFont("Arial", 16))
    top_grid.addWidget(moves_label, 0, 0)
    
    # Adding a button that displays a pop-up with instructions
    instructions_button = QPushButton("How to play")
    instructions_button.clicked.connect(on_help_button_click)
    top_grid.addWidget(instructions_button, 0, 1)
    
    # Adding numbers to grid
    for i in range(0, BOARD_SIZE):
        for j in range(0, BOARD_SIZE):
            if board[i][j] == 0:
                grid.addWidget(QPushButton(' '), i, j)
                grid.itemAtPosition(i, j).widget().clicked.connect(
                    lambda: on_blank_button_click(board, grid)  # Pass parameters to function reference
                )
            else:
                grid.addWidget(QPushButton(f'{board[i][j]}'), i, j)
            
    
    
    # Show the window
    window.setLayout(root_layout)
    window.show()
    sys.exit(app.exec_())

'''Blank Button Click Method - Called after clicking the blank button, turns on the event listeners
for the appropriate number buttons
Parameters: The board (b), grid layout (g), and pair of the row of the blank and column of the blank'''
def on_blank_button_click(b, g):
    i, j = find_num(b, 0)  # Find position of blank space
    print(f"Blank clicked: {i, j}")
    
    #Turning on button click listeners for adjacent buttons
    if 0 < i:  # If the blank can move left
        g.itemAtPosition(i-1, j).widget().clicked.connect(
            lambda: on_num_button_click(b, g, i, j)
        )
    if i > 3:  # If the blank can move right
        g.itemAtPosition(i+1, j).widget().clicked.connect(
            lambda: on_num_button_click(b, g, i, j)
        )
    if 0 < j:  # If the blank can move down
        g.itemAtPosition(i, j-1).widget().clicked.connect(
            lambda: on_num_button_click(b, g, i, j)
        )
    if j > 3:  # If the blank can move up
        g.itemAtPosition(i, j+1).widget().clicked.connect(
            lambda: on_num_button_click(b, g, i, j)
        )
    
        
'''Number Button Click Method - Turns off all button listeners and swaps numbers
Parameters: board (b), grid layout (g), row of blank (i), col of blaml (j)'''
def on_num_button_click(b, g, i, j):
    # Get the current button & it's number
    clicked_button = sender()
    clicked_button_number = int(clicked_button.text())
    
    # Turn off all number button listeners
    if 0 < i:  # If the blank can move left
        g.itemAtPosition(i-1, j).widget().clicked.disconnect()
    if i > 3:  # If the blank can move right
        g.itemAtPosition(i+1, j).widget().clicked.disconnect()
    if 0 < j:  # If the blank can move down
        g.itemAtPosition(i, j-1).widget().clicked.disconnect()
    if j > 3:  # If the blank can move up
        g.itemAtPosition(i, j+1).widget().clicked.disconnect()
        
    # Swap the number values on the grid
    g.itemAtPosition(i, j).widget().setText(clicked_button_number)  # Move number to blank
    clicked_button.setText(0)  # Move blank to number
    
    # Swap the number values on the board
    x, y = find_num(b, clicked_button_number)
    print(f"X, y: {x}, {y}")
    b[x][y] = 0
    print(f"i, j: {i}, {j}")
    b[i][j] = clicked_button_number
    
    # Check for win
    if is_solved():
        pass #placeholder for now
    


'''Help Button Click Method - Displays directions for the game'''
def on_help_button_click():
    # Help instructions string
    m = " ---------------- Instructions ---------------- \n \
        Goal: Slide the puzzle pieces together to order the numbers from 1-15, with the bottom right tile being an empty space. \n \
        How to play: Start by clicking on the empty space, followed by an adjacent number to swap. Once the game is complete and you won, a message will be displayed. \n \
        Move Counter: This will display how many moves you have made in the current game. An optional goal is to minimize these moves."
    #Making a message box and displaying it
    message = QMessageBox()
    message.setStyleSheet("background-color: #1c1c1c; color: white; font-family: Courier New; font-size: 14px;")
    message.setText(m)
    message.setWindowTitle("15-Game Instructions")
    message.resize(800, 800)
    message.show()
    message.exec_()
   
   
# Good practice
if __name__ == '__main__':
    main()
    