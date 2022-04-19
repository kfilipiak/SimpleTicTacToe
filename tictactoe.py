# Entering the contents of the fields on the board
print("Enter cells: ")
cells = '_________'

# Number of wins
winX = 0
winO = 0

# Game board
def game_board(points):
    print('---------')
    print('|', points[0], points[1], points[2], '|')
    print('|', points[3], points[4], points[5], '|')
    print('|', points[6], points[7], points[8], '|')
    print('---------')

game_board(cells)

# Entering the coordinates
def enter_coords():
    while True: 
        coords = input("Enter the coordinates: ")
        # Check if input is a number
        try:
            c1 = int(coords[0])
        except ValueError:
            print("You should enter numbers!")
            continue
        
        # Check if input is two numbers separated by space
        if len(coords) <= 1 or len(coords) == 2 or len(coords) >= 4 or coords[1] != " ": 
            print("Please enter two values separated by space: ")
        # Check if input is in the range from 1 to 3
        else:
            c1 = int(coords[0])
            c2 = int(coords[2])
            if (c1 < 1 or c2 < 1) or (c1 > 3 or c2 > 3):
                print("Coordinates should be from 1 to 3!")
            else:
                break  
    return (coords)

#  Placing the pawn
def placeXO(pawn, x, y, cells):
    while True:
        newcells = ""
        for i in range(0, 3, 1):
            if x == 1 and y == (i + 1):  # First column
                if cells[i] == "_":
                    newcells = newcells + pawn
                elif cells[i] == "X" or cells[i] == "O":
                    print("This cell is occupied! Choose another one!")
                    return(0)
            else:
                newcells = newcells + cells[i]

        for i in range(0, 3, 1):
            if x == 2 and y == (i + 1):  # Second column
                if cells[i + 3] == "_":
                    newcells = newcells + pawn
                elif cells[i + 3] == "X" or cells[i + 3] == "O":
                    print("This cell is occupied! Choose another one!")
                    return(0)
            else:
                newcells = newcells + cells[i + 3]

        for i in range(0, 3, 1):
            if x == 3 and y == (i + 1):  # Third column
                if cells[i + 6] == "_":
                    newcells = newcells + pawn
                elif cells[i + 6] == "X" or cells[i + 6] == "O":
                    print("This cell is occupied! Choose another one!")
                    return(0)
            else:
                newcells = newcells + cells[i + 6]
        if cells == newcells:
            print("This cell is occupied! Choose another one!")
            crd = enter_coords()
            x = int(crd[0])
            y = int(crd[2])
        else:
            cells = newcells
            return(cells)
            
# Checking the state of the game
def game_info(cells, winX, winO):
    # Number of Xs and Os on the board
    zX = 0
    zO = 0
    end = False
    # Winning counter
    if winX > 0 or winO > 0:
        end = True
    else:
        for y in range(0, 9):
            if cells[y] == "X":  # counting Xs
                zX += 1
            elif cells[y] == "O":  # counting Os
                zO += 1
        if zX + zO == 9:
            end = True



    # Game informations
    if end == True:  # End game?
        if winX == 1 and winO == 0:  # X wins
            return("X wins")
        elif (winO == 1 and winX == 0):  # O wins
            return("O wins")
        elif winX + winO > 1:  # X and O win
            return("Impossible")
        elif (winX + winO == 0):  # neither X nor O win                
            if (zO + zX == 9 and abs(zO - zX) < 2):  # board is full and nobody wins
                return("Draw")
            elif abs(zO - zX) >= 2:  # there is more Xs than Os or more Os than Xs
                return("Impossible")
    else: return(0)

# Checking if somebody wins the game
def conditions(cells):
    # Conditions
    for x in range(0, 3, 1):
        if ((cells[3 * x] != '_') and (
                cells[3 * x] == cells[3 * x + 1] and cells[3 * x + 1] == cells[3 * x + 2])):  # horizontal
            if (cells[3 * x] == "X"):
                return("winX")
            elif (cells[3 * x] == "O"):
                return("winO")
        elif ((cells[x] != '_') and (cells[x] == cells[x + 3] and cells[x + 3] == cells[x + 6])):  # vertical
            if (cells[x] == "X"):
                return("winX")
            elif (cells[x] == "O"):
                return("winO")
        elif x == 0 and ((cells[x] != '_') and (
                cells[x] == cells[x + 4] and cells[x + 4] == cells[x + 8])):  # diagonally from left to right
            if (cells[0] == "X"):
                return("winX")
            elif (cells[0] == "O"):
                return("winO")
        elif x == 2 and ((cells[x] != '_') and (
                cells[x] == cells[x + 2] and cells[x + 2] == cells[x + 4])):  # diagonally from right to left
            if (cells[2] == "X"):
                return("winX")
            elif (cells[2] == "O"):
                return("winO")

# Game loop
while True:
    crd = enter_coords()
    x = int(crd[0])
    y = int(crd[2])
    pawnX = "X"
    pawnO = "O"
    # User input
    # Selecting the correct field on the board, check the field and if its empty type X
    ncells = cells
    cells = placeXO(pawnX, x, y, cells)
    while cells == 0:
        crd = enter_coords()
        x = int(crd[0])
        y = int(crd[2])
        cells = placeXO(pawnX, x, y, ncells)

    game_board(cells)
    if conditions(cells) == "winX":
        winX += 1
        end = True
    elif conditions(cells) == "winO":
        winO += 1
        end = True
    
    if game_info(cells, winX, winO) != 0:
        print(game_info(cells, winX, winO))
        break
    
    # User input
    # Selecting the correct field on the board, check the field and if its empty type O
    crd = enter_coords()
    x = int(crd[0])
    y = int(crd[2])
    ncells = cells
    cells = placeXO(pawnO, x, y, cells)
    while cells == 0:
        crd = enter_coords()
        x = int(crd[0])
        y = int(crd[2])
        cells = placeXO(pawnO, x, y, ncells)
    
    game_board(cells)
    if conditions(cells) == "winX":
        winX += 1
    elif conditions(cells) == "winO":
        winO += 1
    
    if game_info(cells, winX, winO) != 0:
        print(game_info(cells, winX, winO))
        break