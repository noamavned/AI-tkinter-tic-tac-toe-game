from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont


turn = "X"
board = []
player, opponent = "o", "x"


def isMovesLeft(board):

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                return True
    return False


def evaluate(b):
    for row in range(3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == player:
                return 10
            elif b[row][0] == opponent:
                return -10

    for col in range(3):

        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

            if b[0][col] == player:
                return 10
            elif b[0][col] == opponent:
                return -10

    # Checking for Diagonals for X or O victory.
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

        if b[0][0] == player:
            return 10
        elif b[0][0] == opponent:
            return -10

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

        if b[0][2] == player:
            return 10
        elif b[0][2] == opponent:
            return -10

    return 0


def minimax(board, depth, isMax):
    score = evaluate(board)

    if score == 10:
        return score

    if score == -10:
        return score

    if isMovesLeft(board) == False:
        return 0

    if isMax:
        best = -1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == "_":

                    board[i][j] = player

                    best = max(best, minimax(board, depth + 1, not isMax))

                    board[i][j] = "_"
        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == "_":

                    board[i][j] = opponent

                    best = min(best, minimax(board, depth + 1, not isMax))

                    board[i][j] = "_"
        return best


def checkBestMove(bm):
    if(bm[0] == 0) and (bm[1] == 0):
        return 0
    elif(bm[0] == 0) and (bm[1] == 1):
        return 1
    elif(bm[0] == 0) and (bm[1] == 2):
        return 2
    elif(bm[0] == 1) and (bm[1] == 0):
        return 3
    elif(bm[0] == 1) and (bm[1] == 1):
        return 4
    elif(bm[0] == 1) and (bm[1] == 2):
        return 5
    elif(bm[0] == 2) and (bm[1] == 0):
        return 6
    elif(bm[0] == 2) and (bm[1] == 1):
        return 7
    elif(bm[0] == 2) and (bm[1] == 2):
        return 8


def findBestMove(board):
    board = createBoard()
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):

            if board[i][j] == "_":

                board[i][j] = player

                moveVal = minimax(board, 0, False)

                board[i][j] = "_"

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    bmindex = checkBestMove(bestMove)
    return bmindex


def createBoard():
    l = []
    for s in board:
        l.append(s['text'].lower())
    for slot in range(len(l)):
        if l[slot] == '':
            l[slot] = "_"
    return [[l[0], l[1], l[2]],
            [l[3], l[4], l[5]],
            [l[6], l[7], l[8]]]



def turnCheck():
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"


def slotCheck(pos):
    if board[pos - 1]["text"] == '':
        return True
    return False


def endGame(state, pos):
    for ps in pos:
        board[ps]['bg'] = 'red'
    if(state == 'O'):
        messagebox.showinfo(
            "BOT WON", "The bot is the one who won this round!")
    elif(state == 'X'):
        messagebox.showinfo(
            "HUMAN WON", "The human is the one who won this round!")
    else:
        for btn in board:
            btn["bg"] = "red"
        messagebox.showinfo("DRAW", "It's a draw!")
    for btn in board:
        btn["state"] = "disabled"


def draw():
    for slot in board:
        if(slot['text'] == ''):
            return False
    return True


def checkWin():
    if board[0]["text"] == board[1]["text"] == board[2]["text"] == "X":
        endGame("X", [0, 1, 2])
        return True
    elif board[0]["text"] == board[1]["text"] == board[2]["text"] == "O":
        endGame("O", [0, 1, 2])
        return True

    elif board[3]["text"] == board[4]["text"] == board[5]["text"] == "X":
        endGame("X", [3, 4, 5])
        return True
    elif board[3]["text"] == board[4]["text"] == board[5]["text"] == "O":
        endGame("O", [3, 4, 5])
        return True

    elif board[6]["text"] == board[7]["text"] == board[8]["text"] == "X":
        endGame("X", [6, 7, 8])
        return True
    elif board[6]["text"] == board[7]["text"] == board[8]["text"] == "O":
        endGame("O", [6, 7, 8])
        return True

    elif board[0]["text"] == board[3]["text"] == board[6]["text"] == "X":
        endGame("X", [0, 3, 6])
        return True
    elif board[0]["text"] == board[3]["text"] == board[6]["text"] == "O":
        endGame("O", [0, 3, 6])
        return True

    elif board[1]["text"] == board[4]["text"] == board[7]["text"] == "X":
        endGame("X", [1, 4, 7])
        return True
    elif board[1]["text"] == board[4]["text"] == board[7]["text"] == "O":
        endGame("O", [1, 4, 7])
        return True

    elif board[2]["text"] == board[5]["text"] == board[8]["text"] == "X":
        endGame("X", [2, 5, 8])
        return True
    elif board[2]["text"] == board[5]["text"] == board[8]["text"] == "O":
        endGame("O", [2, 5, 8])
        return True

    elif board[0]["text"] == board[4]["text"] == board[8]["text"] == "X":
        endGame("X", [0, 4, 8])
        return True
    elif board[0]["text"] == board[4]["text"] == board[8]["text"] == "O":
        endGame("O", [0, 4, 8])
        return True

    elif board[2]["text"] == board[4]["text"] == board[6]["text"] == "X":
        endGame("X", [2, 4, 6])
        return True
    elif board[2]["text"] == board[4]["text"] == board[6]["text"] == "O":
        endGame("O", [2, 4, 6])
        return True

    elif(draw()):
        endGame("draw", [])
        return True
    return False


def compMove():
    bm = findBestMove(1)
    board[bm]['text'] = 'O'
    if(checkWin() == False):
        turnCheck()


def playerMove(pos):
    if turn == "X":
        if slotCheck(pos):
            board[pos - 1]["text"] = "X"
            if(checkWin() == False):
                turnCheck()
                compMove()


def chooseStart():
    global turn
    if (choiceBH.get() == 1):
        turn = 'O'
    else:
        turn = 'X'
    root2.destroy()


root2 = Tk()
root2.title("Choose who starts")
width = 250
height = 75
screenwidth = root2.winfo_screenwidth()
screenheight = root2.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
root2.geometry(alignstr)
root2.resizable(width=False, height=False)

choiceBH = IntVar()

botStart = Radiobutton(root2, font=tkFont.Font(family='Times', size=10),
                       fg="#333333", justify='center', text='Bot', value=True, variable=choiceBH)
botStart.place(x=0, y=10, width=85, height=25)

humanStart = Radiobutton(root2, font=tkFont.Font(family='Times', size=10),
                         fg="#333333", justify='center', text='Human', value=False, variable=choiceBH)
humanStart.place(x=10, y=40, width=85, height=25)

btnr2 = Button(root2, command=lambda: chooseStart(), bg="#efefef", font=tkFont.Font(
    family='Times', size=10), justify='center', text='Start')
btnr2.place(x=110, y=10, width=120, height=50)

root2.mainloop(0)



root = Tk()
root.title("tic tac toe")
width = 299
height = 298
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = "%dx%d+%d+%d" % (
    width,
    height,
    (screenwidth - width) / 2,
    (screenheight - height) / 2,
)
root.geometry(alignstr)
root.resizable(width=False, height=False)

for i in range(9):
    board.append(
        Button(
            root,
            bg="#efefef",
            font=tkFont.Font(family="Times", size=10),
            justify="center",
            text="",
            relief="groove",
        )
    )
board[0].place(x=0, y=-1, width=100, height=100)
board[1].place(x=100, y=-1, width=100, height=100)
board[2].place(x=200, y=-1, width=100, height=100)
board[3].place(x=0, y=99, width=100, height=100)
board[4].place(x=100, y=99, width=100, height=100)
board[5].place(x=200, y=99, width=100, height=100)
board[6].place(x=0, y=199, width=100, height=100)
board[7].place(x=100, y=199, width=100, height=100)
board[8].place(x=200, y=199, width=100, height=100)

board[0]["command"] = lambda: playerMove(1)
board[1]["command"] = lambda: playerMove(2)
board[2]["command"] = lambda: playerMove(3)
board[3]["command"] = lambda: playerMove(4)
board[4]["command"] = lambda: playerMove(5)
board[5]["command"] = lambda: playerMove(6)
board[6]["command"] = lambda: playerMove(7)
board[7]["command"] = lambda: playerMove(8)
board[8]["command"] = lambda: playerMove(9)

if(turn == 'O'):
    compMove()

root.mainloop()
