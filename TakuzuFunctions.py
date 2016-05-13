'''
This .py file contains all functions and variables of the game's program
The main program file is TakuzuMain.py which will be calling this one
For functions' name we've uses PascalCase convention, camelCase for variables and constant variables are in capital letters 
For more details, please find the technical document 
'''


import sys, time, random, pygame
from pygame.locals import *


WHI = (255, 255, 255)
GRE = (200, 200, 200)   #Grey color
YEL = (255, 255, 0)
BLU = (0, 0, 255)
RED = (255, 0, 0)
BLA = (0, 0, 0)

WINDOWWIDTH = 640
WINDOWHEIGHT = 480

mainWindow = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
fullBackground = pygame.image.load("files/greenspin.jpg")
winIcon = pygame.image.load("files/takicon.png")
pygame.display.set_caption("TAKUZU")
pygame.display.set_icon(winIcon)
fpsClock = pygame.time.Clock()
FPS = 30


def DisplayMainMenu():

    ''' Please note that in each sheet of the game, we predefine some fonts which will be used
    So we'll be using only these ones for design purposes and simplicity '''

    mainWindow.blit(fullBackground, (0, 0))
    myFont1 = pygame.font.Font("files/forte.ttf", 120)
    myFont2 = pygame.font.Font("files/bauhs93.ttf", 40)
    myFont3 = pygame.font.Font("files/bauhs93.ttf", 20)
    DisplayText(WINDOWWIDTH//1.95, WINDOWHEIGHT//2.95, myFont1, BLA, "TAKUZU")   #shadow effect
    DisplayText(WINDOWWIDTH//2, WINDOWHEIGHT//3, myFont1, BLU, "TAKUZU")
    DisplayText(WINDOWWIDTH//1.75, 210, myFont3, WHI, "a logic-based number placement game")
        
    pygame.draw.rect(mainWindow, BLA, (WINDOWWIDTH//3+2, 253, WINDOWWIDTH//3, 50))
    pygame.draw.rect(mainWindow, GRE, (WINDOWWIDTH//3, 250, WINDOWWIDTH//3, 50))  
    pygame.draw.rect(mainWindow, BLA, (WINDOWWIDTH//3+2, 323, WINDOWWIDTH//3, 50))
    pygame.draw.rect(mainWindow, GRE, (WINDOWWIDTH//3, 320, WINDOWWIDTH//3, 50))
    DisplayText(WINDOWWIDTH/2, 273, myFont2, BLA, "p l a y")
    DisplayText(WINDOWWIDTH/2, 345, myFont2, BLA, "h e l p")
    
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                if x in range(213, 426) and y in range(250, 300):
                    PlayingGame()                        #Go to level choice menu
                elif x in range(213, 426) and y in range(320, 370):
                    DisplayRules()                       #Go to rules sheet
            
            ''' We are monitoring the mouse motion in order to 
            put a focus while hovering buttons '''
            if event.type == MOUSEMOTION:
                a, b = event.pos
                if a in range(213, 426) and b in range (250, 300):
                    FocusOn(RED, 213, 250)
                elif a in range(213, 426) and b in range (320, 370):
                    FocusOn(RED, 213, 320)
                else:
                    FocusOn(GRE, 213, 250)
                    FocusOn(GRE, 213, 320)
            
        pygame.display.update()


def DisplayRules():
    
    mainWindow.blit(fullBackground, (0, 0))
    myFont1 = pygame.font.Font("files/bauhs93.ttf", 60)
    myFont2 = pygame.font.Font("files/bauhs93.ttf", 20)
    myFont3 = pygame.font.Font("files/trebucbd.ttf", 15)

    pygame.draw.rect(mainWindow, BLA, (17, 35, 80, 22))
    pygame.draw.rect(mainWindow, GRE, (15, 33, 80, 22))
    pygame.draw.rect(mainWindow, BLA, (542, 432, 80, 22))
    pygame.draw.rect(mainWindow, GRE, (540, 430, 80, 22))
    pygame.draw.polygon(mainWindow, GRE, ((5, 40),(20, 25),(20, 60)))
        
    DisplayText(WINDOWWIDTH//2, WINDOWHEIGHT//14, myFont1, WHI, "game rules")
    DisplayText(52, 42, myFont2, WHI, "menu")
    DisplayText(580, 438, myFont2, WHI, "play")
    DisplayText(WINDOWWIDTH//2, 130, myFont2, WHI, "The goal is to fill all white squares with red")
    DisplayText(WINDOWWIDTH//2, 160, myFont2, WHI, "and blue colors by following below rules:")
    DisplayText(WINDOWWIDTH//2, 210, myFont2, WHI, "Each row/column must have an equal number of both colors")
    DisplayText(WINDOWWIDTH//2, 240, myFont2, WHI, "Each row and colum must be unique")
    DisplayText(WINDOWWIDTH//2, 270, myFont2, WHI, "No more than two identical adjacent colors")
    DisplayText(WINDOWWIDTH//2, 320, myFont2, WHI, "Please note that at any time you can")
    DisplayText(WINDOWWIDTH//2, 350, myFont2, WHI, "undo last move or ask for a hint.")
    DisplayText(WINDOWWIDTH//2, 465, myFont3, BLU, "Feedback and support: 162350@supinfo.com")

    for y in range(60, 460, 340):
        for x in range(50, 530, 90):
            pygame.draw.rect(mainWindow, RED,(x, y, 30, 20)) 
            pygame.draw.rect(mainWindow, WHI,(x+30, y, 30, 20), 1)
            pygame.draw.rect(mainWindow, BLU,(x+60, y, 30, 20))
    
    while True:        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONUP:		
                x, y = event.pos
                if x in range (17, 97) and y in range (35, 57):
                    DisplayMainMenu()                   #Go back to the main menu
                if x in range(540, 620) and y in range(430, 452):
                    PlayingGame()                       #Go to level choice menu
        
        pygame.display.update()


'''
In the DisplayText function, we configure as many parametres as possible
So we can easily customize any text by passing in parametres, cordinates of text (the center in our case),
the font, the size, the color and the text to be displayed '''

def DisplayText(x, y, fontUsed, textColor, textToDisplay):
    
    textSurf = fontUsed.render(textToDisplay, True, textColor)
    textRect = textSurf.get_rect()
    textRect.center = (x, y)            #we use .center parameter to easily center texts
    mainWindow.blit(textSurf, textRect)


def FocusOn(COLOR, x, y):               #function used to show a focus on a hovered button
    
    pygame.draw.rect(mainWindow, COLOR, (x, y, 212, 49), 2)


def ChooseLevel():
    
    mainWindow.blit(fullBackground, (0, 0))
    myFont1 = pygame.font.Font("files/bauhs93.ttf", 50)
    myFont2 = pygame.font.Font("files/bauhs93.ttf", 40)
    myFont3 = pygame.font.Font("files/bauhs93.ttf", 20)
    gameLevel = 0

    pygame.draw.rect(mainWindow, BLA,(17, 35, 80, 22))
    pygame.draw.rect(mainWindow, GRE,(15, 33, 80, 22))
    pygame.draw.polygon(mainWindow, GRE,((5, 40),(20, 25),(20, 60)))
    DisplayText(52, 42, myFont3, WHI, "menu")
    
    DisplayText(WINDOWWIDTH//2+3, 123, myFont1, BLA, "Please select a level") #shadow effect
    DisplayText(WINDOWWIDTH//2, 120, myFont1, WHI, "Please select a level")    
    pygame.draw.rect(mainWindow, BLA,(WINDOWWIDTH//3+3, 183, WINDOWWIDTH//3, 50)) 
    pygame.draw.rect(mainWindow, GRE,(WINDOWWIDTH//3, 180, WINDOWWIDTH//3, 50))
    pygame.draw.rect(mainWindow, BLA,(WINDOWWIDTH//3+3, 253, WINDOWWIDTH//3, 50))
    pygame.draw.rect(mainWindow, GRE,(WINDOWWIDTH//3, 250, WINDOWWIDTH//3, 50))  
    pygame.draw.rect(mainWindow, BLA,(WINDOWWIDTH//3+3,323, WINDOWWIDTH//3, 50))
    pygame.draw.rect(mainWindow, GRE,(WINDOWWIDTH//3, 320, WINDOWWIDTH//3, 50))
    pygame.draw.rect(mainWindow, BLA,(WINDOWWIDTH//3+3,393, WINDOWWIDTH//3, 50))
    pygame.draw.rect(mainWindow, GRE,(WINDOWWIDTH//3, 390, WINDOWWIDTH//3, 50))

    DisplayText(WINDOWWIDTH//2, 205, myFont2, BLU, "Grid 4x4")
    DisplayText(WINDOWWIDTH//2, 275, myFont2, BLU, "Grid 6x6")
    DisplayText(WINDOWWIDTH//2, 345, myFont2, BLU, "Grid 8x8")
    DisplayText(WINDOWWIDTH//2, 415, myFont2, BLU, "Grid 10x10")
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == MOUSEBUTTONUP:
                x, y = event.pos
                    
                if x in range (213, 425) and y in range (180, 230):
                    gameLevel = 4
                elif x in range (213, 425) and y in range (250, 300):
                    gameLevel = 6
                elif x in range (213, 425) and y in range (320, 370):
                    gameLevel = 8
                elif x in range (213, 425) and y in range (390, 440):
                    gameLevel = 10
                elif x in range (17, 97) and y in range (35, 57):
                    DisplayMainMenu()                   #Go back to the main menu
        
            if event.type == MOUSEMOTION:
                a, b = event.pos
                
                if a in range(213, 425) and b in range (180, 230):
                    FocusOn(RED, WINDOWWIDTH//3, 180)
                elif a in range(213, 425) and b in range (250, 300):
                    FocusOn(RED, WINDOWWIDTH//3, 250)
                elif a in range(213, 425) and b in range (320, 370):
                    FocusOn(RED, WINDOWWIDTH//3, 320)
                elif a in range(213, 425) and b in range (390, 440):
                    FocusOn(RED, WINDOWWIDTH//3, 390)
                else:
                    FocusOn(GRE, WINDOWWIDTH//3, 180)
                    FocusOn(GRE, WINDOWWIDTH//3, 250)
                    FocusOn(GRE, WINDOWWIDTH//3, 320)
                    FocusOn(GRE, WINDOWWIDTH//3, 390)

            if gameLevel != 0:
                return gameLevel
        
        pygame.display.update()


'''
in below function, we generate all binary numbers (from 0 to 2 to the power level (2**level)
in 00111011 format then we'll keep only the ones respecting 3 game's rules
We'll sometimes convert back these BIN numbers to DEC in order to choose the ones will respect rules together
Finally within these BIN numbers we'll randomly select a spectif number (level chosen) to create
3 two-dimension lists, which we'll be using during the entire game
Please note that within the GenerateBoard function, we'll create and manage many temporary lists
which names are meaningless such as pp, ppp, board... '''

def GenerateBoard(gameLevel):
        
    fmt = "{0:0"+str(gameLevel)+"b}"
    pp = [fmt.format(i) for i in range(2**gameLevel)]     #generate binary number in 0011010 format
    ppp = []

    for i in pp:
        summ = 0
        if "111" not in i and "000" not in i:       #put aside all BIN numbers with 000... or 111...
            for j in range(gameLevel):
                summ += int(i[j])
            if summ == gameLevel//2:                #keeps only the ones with equal number of 0 and 1
                ppp.append(i)

    board = random.sample(ppp, gameLevel)           #we randomly pick n of them (n = level)
    boardDec = [int(n, 2) for n in board]           #convert back to DEC number in order to remove conflicting one
    finalBoard = []

    while True:                                     #We order each line of the board to respect all rules
        m = 2**gameLevel - 1                        
        finalBoard.append(boardDec.pop())
        finalBoard.append(boardDec.pop())
        
        if finalBoard[0] + finalBoard[1] == m:
            finalBoard.append(boardDec.pop())
            finalBoard.append(m - finalBoard[2])
            if finalBoard[3] in boardDec:
                boardDec.remove(finalBoard[3])
        else:
            finalBoard.append(m - finalBoard[1])
            finalBoard.append(m - finalBoard[0])
            if finalBoard[2] in boardDec:
                boardDec.remove(finalBoard[2])
            if finalBoard[3] in boardDec:
                boardDec.remove(finalBoard[3])

        if len(finalBoard) == gameLevel:            #In case of grid 4x4, we stop here
            break
        else:
            finalBoard.insert(-1, boardDec.pop())
            finalBoard.insert(-1, (m - finalBoard[-2]))
            if finalBoard[-1] in boardDec:
                boardDec.remove(finalBoard[-1])
                
        if len(finalBoard) == gameLevel:            #In case of grid 6x6, we stop here...
            break
        else:
            finalBoard.insert(-1, boardDec.pop())
            finalBoard.insert(-1, (m - finalBoard[-2]))
            if finalBoard[-1] in boardDec:
                boardDec.remove(finalBoard[-1])
                
        if len(finalBoard) == gameLevel:
            break
        else:
            finalBoard.insert(-1, boardDec.pop())
            finalBoard.insert(-1, (m - finalBoard[-2]))
        break

    board = [fmt.format(i) for i in finalBoard]   #bring it back to BIN format

    ''' during the entire game, we will be using these 3 2D lists
    gameBoard, unsolved which is the main list, in which all player's input will be saved
    gameBoard1, solved grid, will be used in read only mode
    gameBoard2, is a copy of gameBoard, used in read only, to keep the initial state of gameBoard '''
    
    gameBoard = [[int(n) for n in m] for m in board]
    gameBoard1 = [[int(n) for n in m] for m in board]
    gameBoard2 = [[int(n) for n in m] for m in board]
    
    for i in range(gameLevel):
        k = random.sample(range(gameLevel), gameLevel//2)   #we use the "9" figure for white (hidden) cells
        for j in k:
            gameBoard[i][j] = 9
            gameBoard2[i][j] = 9
    #we randomly hide some cells by affecting them value 9
            
    return gameBoard, gameBoard1, gameBoard2


'''
lifoTable is a list which keeps track of all moves during playing (from player and hints)
It saves all coordinates of values as (a, b) tuples, so we could undo last updates '''

def CleanLast(gameBoard, lifoTable, undoSound):    
    if len(lifoTable) != 0:
        (a, b) = lifoTable.pop()        #Undo last move, we just pick the last tuple from lifoTable
        gameBoard[a][b] = 9
        pygame.mixer.Sound.play(undoSound)
    
    return gameBoard, lifoTable


'''
to show an hint, we pick randomnly a (true) value from gameBoard1 and copy
to the same index in gameBoard '''

def ShowHint(gameBoard, gameBoard1, gameLevel, lifoTable, hintSound):
    k = random.sample(range(gameLevel), gameLevel)
    for i in k:
        for j in k:                     #pick randomly a value from gameBoard1 then copy to gameBoard
            if gameBoard[i][j] == 9:
                gameBoard[i][j] = gameBoard1[i][j]
                lifoTable.append((i, j))
                pygame.mixer.Sound.play(hintSound)
                return gameBoard, lifoTable
    
 
def CheckRule1Row(gameBoard, gameLevel, moveX):      #rule 1a: equal number of 1 and 0 in row
    
    if 9 not in gameBoard[moveX] and sum(gameBoard[moveX]) != gameLevel//2:
        return False	#display "Number of 0 and 1 are not equal in this row"
    
    return True


def CheckRule1Column(gameBoard, gameLevel, moveY):   #rule 1b: equal number of 1 and 0 in column

    tempTable = []      # a temporary list which we'll put all value from this cell's column
    for i in gameBoard:
        tempTable.append(i[moveY])

    if 9 not in tempTable and sum(tempTable) != gameLevel//2:
        return False 	#display "Number of 0 and 1 are not equal in this column"

    return True


'''
Checking rule 2: no identical row or column
In Python, it's easier to browse each row of a 2D list while it's a bit tricky for columns
To do so, we first transpose the 2D list (using loop and list comprehension) to a tempList,
Then we'll apply the same check function '''

def CheckRule2(gameBoard, gameLevel):
    
    for i in range(gameLevel-1): 
        if 9 not in gameBoard[i]:           #We'll compare only full rows (the ones without white cells)
            if gameBoard[i] in gameBoard[i+1:]:
                return False 	#"Duplicate row found!"

    tempTable = []
    for i in range(gameLevel):              #transposing gameBoard to a temporary list
        tempTable.append([j[i] for j in gameBoard])

    for i in range(gameLevel-1): 
        if 9 not in tempTable[i]:           #We'll compare only full columns
            if tempTable[i] in tempTable[i+1:]:
                return False 	#Duplicate column found!

    return True


'''
To check value of neighbour cells, we created 2 lists (of tuples) of neighbours. One for 2 in same side
and another for the 2 surrounding the active cell '''

def CheckRule3(gameBoard, lvl, x, y, value):    #rule 3: no more than two identical adjacent numbers
    
    neighCells = [((x-1, y),(x-2, y)), ((x, y+1),(x, y+2)),((x+1, y),(x+2, y)), ((x, y-1),(x,y-2))]
    
    for (a, b) in neighCells:                   #two next cells in each side
        if a[0] in range(lvl) and a[1] in range(lvl) and b[0] in range(lvl) and b[1] in range(lvl) and value != 9:
            if (value, value) == (gameBoard[a[0]][a[1]], gameBoard[b[0]][b[1]]):
                return False

    neighCells2 = [((x-1, y),(x+1, y)), ((x, y-1),(x, y+1))]
    
    for (a, b) in neighCells2:                  #two cells surrounding
        if a[0] in range(lvl) and a[1] in range(lvl) and b[0] in range(lvl) and b[1] in range(lvl) and value != 9:
            if (value, value) == (gameBoard[a[0]][a[1]], gameBoard[b[0]][b[1]]):
                return False
            
    return True


def UpdatingBoard(gameBoard, gameBoard2, lifoTable, a, b):
    
    if gameBoard2[a][b] == 9:           #Update cell's value only if it was white at the beginning 
        if gameBoard[a][b] == 9:
            gameBoard[a][b] = 1         #change value from 9 to 1 (means color from WHI to RED)
        elif gameBoard[a][b] == 1:
            gameBoard[a][b] = 0
        elif gameBoard[a][b] == 0:
            gameBoard[a][b] = 9
        lifoTable.append((a, b))

    return gameBoard, lifoTable


'''
The player win when gameBoard == gameBoard1
Then he's asked to play again or leave '''

def GameWon():
    
    myFont1 = pygame.font.Font("files/bauhs93.ttf", 30)
    myFont3 = pygame.font.Font("files/bauhs93.ttf", 20)
    DisplayText(282, 422, myFont1, BLA, "\o/  you've won the game  \o/")   #Shadow effect
    DisplayText(280, 420, myFont1, YEL, "\o/  you've won the game  \o/")
    DisplayText(280, 455, myFont3, WHI, "Would you like to play again?")
    
    pygame.draw.rect(mainWindow, BLA,(462, 443, 70, 30))
    pygame.draw.rect(mainWindow, GRE,(460, 440, 70, 30))   #Yes button
    pygame.draw.rect(mainWindow, BLA,(542, 443, 70, 30))
    pygame.draw.rect(mainWindow, GRE,(540, 440, 70, 30))   #No button
    DisplayText(495, 450, myFont1, WHI, "yes")
    DisplayText(575, 452, myFont1, WHI, "no")

    return True


'''    
Below function runs while user is playing. It calls almost all other functions
and will stop running only when user wins (or quit), then prompt for continuing message '''

def PlayingGame():       
    
    myFont1 = pygame.font.Font("files/bauhs93.ttf", 30)
    myFont3 = pygame.font.Font("files/bauhs93.ttf", 20)
    pygame.mixer.music.load("files/theblueststar.mp3")
    hintSound = pygame.mixer.Sound("files/hintsound.wav")
    undoSound = pygame.mixer.Sound("files/undosound.wav")
    
    gameLevel = ChooseLevel()
    pygame.mixer.music.play(-1)

    ''' Despite all checks we've setup while generating boards, we've noticed some cases of
    duplicate column. So we've decided to loop in this next while until we got the perfect board for playing with '''
    
    while True:
        (gameBoard, gameBoard1, gameBoard2) = GenerateBoard(gameLevel)
        if CheckRule2(gameBoard1, gameLevel):
            break
    
    lifoTable = []                      #we initialize the lifoTable for undo purpose
    u, v = 0, 0
    soundStatus = 1

    while True:
        mainWindow.blit(fullBackground, (0, 0))
        pygame.draw.rect(mainWindow,BLA,(103, 43, 360, 360))   #shadow of the board
        cellSize = 360//gameLevel       #we've chosen a 360x360 px board size because 360 is multiple of 4, 6, 8 and 10
                                        #so printing any level in the space frame is easier
        y = 40                          #Distance from the top of the window
        for i in gameBoard:             #these nested loops will display board's cells with their colors
            x = 100                     #Distance from the left border of the window
            for j in i:
                if j == 0:
                    pygame.draw.rect(mainWindow, BLU, (x, y, cellSize, cellSize))
                elif j == 1:
                    pygame.draw.rect(mainWindow, RED, (x, y, cellSize, cellSize))
                else:
                    pygame.draw.rect(mainWindow, WHI, (x, y, cellSize, cellSize))
                
                x += cellSize
            y += cellSize

        y = 40
        for i in range(gameLevel):      #these loops display only black lines between cells
            x = 100
            for j in range(gameLevel):
                pygame.draw.rect(mainWindow, BLA, (x, y, cellSize, cellSize), 1)
                x += cellSize
            y += cellSize
            
        pygame.draw.rect(mainWindow, BLA, (502, 103, 80, 30))
        pygame.draw.rect(mainWindow, GRE, (500, 100, 80, 30))   #hint button  
        pygame.draw.rect(mainWindow, BLA, (502, 153, 80, 30))
        pygame.draw.rect(mainWindow, GRE, (500, 150, 80, 30))   #undo button
        pygame.draw.rect(mainWindow, BLA, (542, 43, 40, 30))
        pygame.draw.rect(mainWindow, GRE, (540, 40, 40, 30))   #sound button
        pygame.draw.rect(mainWindow, BLA, (17, 53, 80, 30))
        pygame.draw.rect(mainWindow, GRE, (15, 50, 80, 30))
        pygame.draw.polygon(mainWindow, GRE,((5, 65), (20, 40), (20, 90)))
        pygame.draw.rect(mainWindow, WHI, (548, 50, 5, 11))
        pygame.draw.polygon(mainWindow, WHI,((555, 50), (562, 45), (562, 65), (555, 60)))
        
        DisplayText(540, 115, myFont1, WHI, "hint")
        DisplayText(540, 165, myFont1, WHI, "undo")
        DisplayText(52, 64, myFont1, WHI, "back")      #back button is used in some sheet to facilitate navigation within the game

        if gameBoard == gameBoard1:
            gameBoard2 = gameBoard1         #Avoid player to modify board when game finished
            lifoTable.clear()               #Also avoid player undo last move
            GameWon()

        ''' below 4 if statements, check the 3 rules of the game then display the error message accordingly
        and leave the message displayed till the next player's move'''
            
        if not CheckRule1Row(gameBoard, gameLevel, u):
            DisplayText(WINDOWWIDTH//2.35, 417, myFont3, RED, "RED/BLUE not equal in this row!")

        if not CheckRule1Column(gameBoard, gameLevel, v):
            DisplayText(WINDOWWIDTH//2.3, 434, myFont3, RED, "RED/BLUE not equal in this column!")

        if not CheckRule2(gameBoard, gameLevel):
            DisplayText(WINDOWWIDTH//2.25, 451, myFont3, RED, "Duplicate row/column found!")

        if not CheckRule3(gameBoard, gameLevel, u, v, gameBoard[u][v]):
            DisplayText(WINDOWWIDTH//2.3, 468, myFont3, RED, "More than 2 adjacent colours!")

        if soundStatus == 0:
            pygame.draw.line(mainWindow,WHI,(565,50),(572,60),4)
            pygame.draw.line(mainWindow,WHI,(565,60),(572,50),4)
            pygame.mixer.music.pause()
        else:
            pygame.draw.line(mainWindow,GRE,(565,50),(572,60),4)
            pygame.draw.line(mainWindow,GRE,(565,60),(572,50),4)
            pygame.mixer.music.unpause()        
         
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == MOUSEBUTTONUP:
                x, y = event.pos

                if x in range (100, 460) and y in range(40, 400):
                    u = int((y - 40)//(360/gameLevel))      #Please note that array's rows indexes come from y coordinates (not x)
                    v = int((x - 100)//(360/gameLevel))     #and vice-versa
                    #lifoTable.append((u, v))
                    
                    UpdatingBoard(gameBoard, gameBoard2, lifoTable, u, v)  #changing value of the cell which will define its colour

                if x in range (500, 580) and y in range (100, 130):
                    ShowHint(gameBoard, gameBoard1, gameLevel, lifoTable, hintSound)
                    
                elif x in range (500, 580) and y in range (150, 190):
                    CleanLast(gameBoard, lifoTable, undoSound)

                elif x in range (17, 97) and y in range (53, 83):   #Back button brings to level selection
                    PlayingGame()
                    
                elif x in range (540, 580) and y in range (40, 70):
                    if soundStatus == 0:
                        soundStatus = 1
                    else:
                        soundStatus = 0
                    
                elif x in range (460, 530) and y in range (440, 470) and gameBoard2 == gameBoard1:  #Player has won and continue
                    PlayingGame()
                 
                elif x in range (540, 610) and y in range (440, 470) and gameBoard2 == gameBoard1:  #Player has won and leave
                    pygame.quit()
                    sys.exit()
                
        pygame.display.update()
        fpsClock.tick(FPS)
