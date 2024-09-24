''' 15-puzzle (sliding puzzle game) - JJ McCauley - Last Update 9/16/24'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from functools import partial  # Passing extra parameters through clicked buttons
import sys
import random as rand  # Shuffling board

# Global Constants
BOARD_SIZE = 4
# Global Variables
buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] # Empty 2d list that will hold the buttons
b_pos = (-1, 1)

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
Returns: Whether the board was solved (True if solved, False if not)'''
def is_solved(board):
    return board == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


'''Helper function that returns if the provided index is 4-way adjacent to the blank
Parameters: i, j
Returns: Wether the given index is adjacent to blank'''
def is_adjacent(i, j, b_pos):
    if i == b_pos[0] and abs(j - b_pos[1]) == 1:  # In the same row and 1 tile apart
        return True
    elif j == b_pos[1] and abs(i - b_pos[0]) == 1:  # In the same column and 1 tile apart
        return True
    else:
        return False


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
    global b_pos  # Declare that b_pos as global for correct referencing
    
    # Getting the solvable board
    board = make_board()
    
    # Making a move counter to display on window
    m_counter = 0
    
    # Making variable to hold the blank position for easy comparison
    b_pos = (-1, -1)  # Initialized with signal values
    
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
                button = QPushButton(' ')
                b_pos = (i, j)
            else:
                button = (QPushButton(f'{board[i][j]}'))
            
            buttons[i][j] = button
            button.clicked.connect(partial(on_num_button_click, i, j, board))  # Pass positional paramters to function
            grid.addWidget(button, i, j)
            
    # Show the window
    window.setLayout(root_layout)
    window.show()
    sys.exit(app.exec_())

        
'''Number Button Click Method - Checks if the current button is adjacent to the blank button.
If it is, swaps values in board and updates GUI 
Parameters: i (row of button clicked), j (column of button clicked), board, b_pos (blank button position)'''
def on_num_button_click(i, j, board):
    global b_pos
    if is_adjacent(i, j, b_pos):
        # Get the current button & it's number
        clicked_button_number = board[i][j]
            
        # Swap the number values on the grid
        buttons[b_pos[0]][b_pos[1]].setText(str(clicked_button_number))  # Move number to blank
        buttons[i][j].setText(' ')  # Move blank to last clicked tile
        
        # Swap the number values on the board
        board[i][j] = 0
        print(f"i, j: {i}, {j}")
        board[b_pos[0]][b_pos[1]] = int(clicked_button_number)
        b_pos = (i, j)
        
        # Check for win
        if is_solved(board):
            pass #placeholder for now
    


'''Help Button Click Method - Displays directions for the game'''
def on_help_button_click():
    # Help instructions string
    m = " ---------------- Instructions ---------------- \n \
        Goal: Slide the puzzle pieces together to order the numbers from 1-15, with the bottom right tile being an empty space. \n \
        How to play: Start by clicking o an adjacent number to swap with the empty space. Once the game is complete and you won, a message will be displayed. \n \
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
    