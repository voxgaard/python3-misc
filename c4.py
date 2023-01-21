#Connect 4 Game.

# Class stack (for each column).
class Stack:
    def __init__(self):
        self._list = []
    
    def __len__(self):
        return len(self._list)    
    
    def push(self, element):
        if len(self._list) <= 6:
            self._list.append(element)
        else:
            return
    
    def checkStack(self):
        return self._list[-1]

# Initialize blank display.
def newDisplay():
    rows = ['a','b','c','d','e','f']
    clearedGameState = []
    for i in range(0,len(rows)):
        clearedGameState.append([' '] * 7)
    
    return clearedGameState

# Initialize empty stacks.
def newStacks():
    clearedStacks = [ Stack(), Stack(), Stack(), 
                    Stack(), Stack(), Stack(), Stack() ]
    return clearedStacks

# Print game status.
def printDisplay(gameState):
    rows = ['a','b','c','d','e','f']
    column = '   1   2   3   4   5   6   7   '
    row = [[n] for n in range(0,7)]
    row[0][0] = ' | '
    row[1][0] = ' | '
    row[2][0] = ' | '
    row[3][0] = ' | '
    row[4][0] = ' | '
    row[5][0] = ' | '
    print('')
    print('  ' + '-'*(len(column)-3))
    for j in range(0,len(rows)):
        for i in range(1,8):
            row[j][0] = row[j][0] + str(gameState[j][i-1]) + ' | '
        print(row[j][0])
        print('  ' + '-'*((len(row[j][0])-3)))
    print(column)
    print('')

# Player(s) Turn.
def turn(token, gameState, Stacks, craven):
    validMoves = {'1','2','3','4','5','6','7','Concede'}
    columnChoice = str(input('The current turn is for: {} ... '.format(token)))
    if (columnChoice in validMoves) == False:
        print('Input must be integer between 1 and 7. ' + \
                'To forfeit type "Concede".')
        turn(token, gameState, Stacks, craven)
    elif columnChoice == 'Concede':
        if token == 'X':
            craven = 'X'
            for j in range(0,6):
                for i in range(0,7):
                    gameState[j][i] = 'O'
        else:
            craven = 'O'
            for j in range(0,6):
                for i in range(0,7):
                    gameState[j][i] = 'X'
        print('The player controlling {} has forfeit the game'.format(token))
    else: 
        columnChoice = int(columnChoice)
        if len(Stacks[columnChoice-1]) < 6:
            Stacks[columnChoice-1].push(token)
            gameState[6-len(Stacks[columnChoice-1])][columnChoice-1] = \
                Stacks[columnChoice-1].checkStack()
        else:
            print('Column full, try again!')
            turn(token, gameState, Stacks, craven)
    return gameState, Stacks, craven

# Check for end of game.
def checkWin(V,gameState,Stacks,counter,stalemate,craven):
    gameOver = False   
    # Horizontal victory condition.
    for j in range(0,6):
        for i in range(3,7):
            if (gameState[j][i]==gameState[j][i-1]==\
                gameState[j][i-2]==gameState[j][i-3]==V):
                    gameOver = True
            else:
                continue   
    # Vertical victory condition.
    for i in range(0,7):
        for j in range(3,6):
            if (gameState[j][i]==gameState[j-1][i]==\
                gameState[j-2][i]==gameState[j-3][i]==V):
                    gameOver = True
            else:
                continue
    # Diagonal victory condition.
    for i in range(0,4):
        for j in range(0,3):
            if (gameState[j][i]==gameState[j+1][i+1]==\
                gameState[j+2][i+2]==gameState[j+3][i+3]==V or
                gameState[j+3][i]==gameState[j+2][i+1]==\
                gameState[j+1][i+2]==gameState[j][i+3]==V):
                    gameOver = True
            else:
                continue
    # Stalemate detection.
    counter = 0
    if len(Stacks[0]) == 6:
        counter = counter + 1
    if len(Stacks[1]) == 6:
        counter = counter + 1
    if len(Stacks[2]) == 6:
        counter = counter + 1
    if len(Stacks[3]) == 6:
        counter = counter + 1
    if len(Stacks[4]) == 6:
        counter = counter + 1
    if len(Stacks[5]) == 6:
        counter = counter + 1
    if len(Stacks[6]) == 6:
        counter = counter + 1
    if counter < 7:
        stalemate = False
    else:
        stalemate = True
        gameOver = True
    # Resolution type detection.
    if gameOver == True and stalemate == True:
        print('Stalemate!')
    if gameOver == True and stalemate == False:
        print(V + ' has achieved victory!')
    if craven == 'X':
        gameOver = True
        print('O has achieved victory!')
    if craven == 'O':
        gameOver = True
        print('X has achieved victory!')
    
    return gameOver

# Game loop.
def gameLoop():
# Set new game.
    gameState = newDisplay()
    Stacks = newStacks()
    printDisplay(gameState)
    print('To move: select a column via input of ' + \
          'corresponding integer (1-7).')
# Game begins looping until a win condition is met.
    gameOver = False
    stalemate = False
    craven = ""
    while gameOver == False:
# X player turn: Input, Update, Check, Proceed if ongoing
        gameState, Stacks, craven = turn('X',gameState,Stacks,craven)
        printDisplay(gameState)
        gameOver = checkWin('X',gameState,Stacks,0,stalemate,craven)
        if gameOver == True:
            break
# O player turn: Input, Update, Check, Proceed if ongoing
        gameState, Stacks, craven = turn('O',gameState,Stacks,craven)
        printDisplay(gameState)
        gameOver = checkWin('O',gameState,Stacks,0,stalemate,craven)
        if gameOver == True:
            break

    print('Game Over')

# Convention to perform call only as script
if __name__ == '__main__':
    gameLoop()