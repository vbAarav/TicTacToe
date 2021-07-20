#Libraries
import pygame
from time import sleep

#Initalise pygame module
pygame.init()

#Load images
boardImg = pygame.image.load('board.png') # Load Board Image
crossImg = pygame.image.load('cross.png') # Load Cross Image
circleImg = pygame.image.load('circle.png') # Load Circle Image

#Variables
gameBoard = [ 
              [0, 0, 0],  # Row 0
              [0, 0, 0],  # Row 1
              [0, 0, 0]   # Row 2
            ]

winStates = [
                #Diagonals
                [(0,0), (1, 1), (2, 2)],
                [(2,0), (1, 1), (0, 2)],

                #Rows
                [(0,0), (0, 1), (0, 2)],
                [(1,0), (1, 1), (1, 2)],
                [(2,0), (2, 1), (2, 2)],

                #Columns
                [(0,0), (1, 0), (2, 0)],
                [(0,1), (1, 1), (2, 1)],
                [(0,2), (1, 2), (2, 2)],                
            ]

drawPos = { 
    (0, 0): (0, 0),
    (0, 1): (64, 0),
    (0, 2): (128, 0),

    (1, 0): (0, 64),
    (1, 1): (64, 64),
    (1, 2): (128, 64),

    (2, 0): (0, 128),
    (2, 1): (64, 128),
    (2, 2): (128, 128),
    }

#Constants
WIDTH = 192
HEIGHT = 192
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LEFT_CLICK = 1
RIGHT_CLICK = 3
RESET = [pygame.K_r]

#Initalise pygame Settings
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Create the pygame window
pygame.display.set_caption('Tic Tac Toe') # Set the caption of the window

#Text Variables
font = pygame.font.Font('freesansbold.ttf', 18) # Initalise the font
textX = 25
textY = 85

#Draw objects
def draw_objects():
    global gameBoard
    screen.blit(boardImg, (0, 0)) # Draw board
    
    for i in range(len(gameBoard)): # Iterate through rows
        for j in range(len(gameBoard)): # Iterate through columns
            if gameBoard[i][j] == 1: # Check if the position is cross
                screen.blit(crossImg, drawPos[(i, j)]) # Draw cross

            if gameBoard[i][j] == 2: # Check if the position is circle
                screen.blit(circleImg, drawPos[(i, j)]) # Draw cross          

#Show Text
def show_text(val):
    label = font.render(val, True, WHITE)
    screen.fill(BLACK)
    screen.blit(label, (textX, textY))    

#Game Loop
gameLoop = True
turn = 1
while gameLoop:
    #Fill screen
    screen.fill(BLACK)

    #Iterate through all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the game is being exited
            gameLoop = False # Escape game loop
            
        #Mouse Press 
        if event.type == pygame.MOUSEBUTTONDOWN: # If a mouse button is being pressed
            mouseX, mouseY = pygame.mouse.get_pos() # Get the position of the mouse
            
            # Iterate through draw positions
            for key in drawPos: 
                if (mouseX >= drawPos[key][0] and mouseX <= drawPos[key][0] + 64) and (mouseY >= drawPos[key][1] and mouseY <= drawPos[key][1] + 64): # Check which box was pressed on the grid
                    if (event.button == LEFT_CLICK) and (gameBoard[key[0]][key[1]] == 0) and (turn == 1): # Check if the requirements match for the value to be changed
                        gameBoard[key[0]][key[1]] = 1 # Change the value of the grid
                        turn = 2
                    elif (event.button == RIGHT_CLICK) and (gameBoard[key[0]][key[1]] == 0) and (turn == 2): # Check if the requirements match for the value to be changed
                        gameBoard[key[0]][key[1]] = 2 # Change the value of the grid 
                        turn = 1
        #Key Press
        if event.type == pygame.KEYDOWN: # If a key is being pressed
            if event.key in RESET:
                gameBoard = [ 
                            [0, 0, 0],  # Row 0
                            [0, 0, 0],  # Row 1
                            [0, 0, 0]   # Row 2
                            ]
                turn = 1

    #Update screen
    draw_objects()

    #Check for winners
    for state in winStates: # Iterate through each possible win state
        temp = [] # Store values in temporary list
        for r, c in state: # Iterate through winning position (row, column) in each state
            if gameBoard[r][c] != 0: # If the box is not empty
                temp.append(gameBoard[r][c]) # Add to temporary list

        #Check if a win state is met
        if temp.count(1) == 3:
            show_text('Player One Wins')
            #gameLoop = False

        if temp.count(2) == 3:
            show_text('Player Two Wins')
            #gameLoop = False   

    pygame.display.update()