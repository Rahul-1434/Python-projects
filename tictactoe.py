import random

board=['-','-','-',
       '-','-','-',
       '-','-','-']
currentplayer='X'
winner=None
Tie=True

def printBoard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("-----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("-----------")
    print(board[6]+" | "+board[7]+" | "+board[8])

def playerinput(board):
    c=0
    while c!=1:
        x=int(input("Enter a number 1-9:"))
        if 1<=x and x<10 and board[x-1]=='-':
            board[x-1]=currentplayer
            c=1
        else:
            print("Oops player is already in that spot!")

def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0]!='-':
        winner=board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]!='-':
        winner=board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]!='-':
        winner=board[6]
        return True

def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!='-':
        winner=board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!='-':
        winner=board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!='-':
        winner=board[2]
        return True

def checkDigonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!='-':
        winner=board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!='-':
        winner=board[2]
        return True

def checkTie(board):
    if '-' not in board:
        print("It's a Tie!")
        global Tie
        Tie=False

def switch():
    global currentplayer
    if currentplayer=='X':
        currentplayer='O'
    else:
        currentplayer='X'

def checkWin():
    if checkDigonal(board) or checkRow(board) or checkColumn(board):
        print(f"The Winner is {winner}")

def computer(board):
    checkWin()
    checkTie(board)
    while currentplayer=='O':
        if Tie==False or winner is not None:
            break
        x=random.randint(0,8)
        if board[x]=='-':
            board[x]='O'
            switch()

while True:
    printBoard(board)
    checkWin()
    if Tie==False or winner is not None:
        break
    playerinput(board)
    switch()
    computer(board)