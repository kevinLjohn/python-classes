import random


board = ["-", "-", "-", "-", "-", "-",
        "-", "-", "-", "-", "-", "-",
        "-", "-", "-", "-", "-", "-",
        "-", "-", "-", "-", "-","-",
        "-", "-", "-", "-", "-","-",
        "-", "-", "-", "-", "-", "-"]
currentPlayer = "A"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] + " | " + board[4])
    print("-----------------")
    print(board[5] + " | " + board[6] + " | " + board[7]  + " | " + board[8] + " | " + board[9])
    print("-----------------")
    print(board[10] + " | " + board[11] + " | " + board[12] + " | " + board[13] + " | " + board[14])
    print("-----------------")
    print(board[15] + " | " + board[16] + " | " + board[17] + " | " + board[18] + " | " + board[19])
    print("-----------------")
    print(board[20] + " | " + board[21] + " | " + board[22] + " | " + board[23] + " | " + board[24])
    print("-----------------")
    print(board[25] + " | " + board[26] + " | " + board[27] + " | " + board[28] + " | " + board[29])


def playerInput(board):
    inp = int(input("Select a spot 1-29: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")



def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


def switchPlayer():
    global currentPlayer
    if currentPlayer == "A":
        currentPlayer = "Z"
    else:
        currentPlayer = "A"


def computer(board):
    while currentPlayer == "Z":
        position = random.randint(0, 30)
        if board[position] == "-":
            board[position] = "Z"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)

