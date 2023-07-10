import random, copy

def drawBoard(board):
    print(f"{board['top-L']} | {board['top-M']} | {board['top-R']}")
    print(f"--------")
    print(f"{board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print(f"--------")
    print(f"{board['low-L']} | {board['low-M']} | {board['low-R']}")


# Get Player's Letter Choice
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
#first letter in tuple is player's, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
# Function to randomly decide who goes first
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

# Function to check if the player wants to play again
def playAgain():
    print(f"Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

# Function to make a move on the board
def makeMove(board, letter, move):
    board[move] = letter

# Function to check if a player has won
def isWinner(bo, le):
    return ((bo['top-L'] == le) and (bo['top-M'] == le) and (bo['top-R'] == le) or ##across top
(bo['mid-L'] == le) and (bo['mid-M'] == le) and (bo['mid-R'] == le) or ##across middle
(bo['low-L'] == le) and (bo['low-M'] == le) and (bo['low-R'] == le) or ##across bottom
(bo['top-L'] == le) and (bo['mid-L'] == le) and (bo['low-L'] == le) or ##down left
(bo['top-M'] == le) and (bo['mid-M'] == le) and (bo['low-M'] == le) or ##down middle
(bo['top-R'] == le) and (bo['mid-R'] == le) and (bo['low-R'] == le) or ##down right
(bo['top-L'] == le) and (bo['mid-M'] == le) and (bo['low-R'] == le) or ##diagonal
(bo['top-R'] == le) and (bo['mid-M'] == le) and (bo['low-L'] == le))  ##diagonal

# Function to check if a space on the board is free
def isSpaceFree(board, move):
    return board[move] == ''

# Function to get the player's next move
def getPlayerMove(board):
    move = ''
    while move not in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() or not isSpaceFree(board, move):
        print('What is your next move? (top-, mid-, low- & L, M, R)')
        move = input()
    return move

# Function to choose a random move from a list of possible moves
def chooseRandomMoveFromList(board, movelist):
    possibleMoves = []
    for i in movelist:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# Function to get the computer's next move
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Check if computer can win in the next move
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, computerLetter, i)
            if isWinner(dupe, playerLetter):
                return i
            
    # Check if player could win in next move and block
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, playerLetter, i)
            if isWinner(dupe, playerLetter):
                return i
            
    # Try to take one of the corners if they are free
    move = chooseRandomMoveFromList(board,['top-L', 'top-R', 'low-L', 'low-R'])
    if move != None:
        return move

    # Try to take center if it is free.
    if isSpaceFree(board, 'mid-M'):
        return 'mid-M'

    # Move on one of the sides.
    return chooseRandomMoveFromList(board,['top-M', 'low-M', 'mid-L', 'mid-R'])

# Function to check if the board is full
def isBoardFull(board):
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        if isSpaceFree(board, i):
            return False
    return True
            
# Main game loop
print(f"Welcome to Tic Tac Toe!")

while True:
    theBoard = {'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': '', 'mid-R': '',
            'low-L': '', 'low-M': '', 'low-R': ''}

    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(f"The {turn} will go first.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray! You have wond the game!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'computer'
        else:
            drawBoard(theBoard)
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The machine has won. Humanity has lost.")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'player'
                  
    if not playAgain():
        break

print("Goodbye!")

