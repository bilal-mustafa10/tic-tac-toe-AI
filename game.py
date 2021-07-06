# Tic-tac-toe Game
#Reference: https://www.techwithtim.net/tutorials/python-programming/tic-tac-toe-tutorial/


import random
global board,playerOneValues,computerValues,values,playerOneTurn,computerTurn,playerOneWin,computerWin,ticTacToe

board = [' ' for x in range(10)]
playerOneValues = []
computerValues = []
values = [1,2,3,4,5,6,7,8,9]
playerOneTurn = False
computerTurn = False
playerOneWin = 0
computerWin = 0
ticTacToe = True


def introduction():
    global playerOneName
    playerOneName = input("Please enter your name: ")
    playerOneName = playerOneName.upper()

def printBoard(board):
    print('\n')
    print("          " +board[1],end = "  |")
    print("  " +board[2],end = "   | ")
    print(" " +board[3])
    print("          " + "--------------")
    print("          " +board[4],end = "  |")
    print("  " +board[5],end = "   | ")
    print(" " +board[6])
    print("          " + "--------------")
    print("          " +board[7],end = "  |")
    print("  " +board[8],end = "   | ")
    print(" " +board[9])

def menu():
    print("=================================================")
    print(playerOneName,"WON: ",playerOneWin,end = "                     ")
    print("COMPUTER WON: ",computerWin)
    print()
    if playerOneTurn == True:
        print(playerOneName,"'s TURN")
    elif computerTurn == True:
        print("COMPUTER's TURN")

def startGame():
    global playerOneTurn,computerTurn
    turn = random.randint(1,2)
    if turn == 1:
        playerOneTurn = True
    elif turn == 2:
        computerTurn = True

def ComputerMove():
    global values
    possibleMoves = values
    move = 0

    # Winning move
    for letter in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWinner(boardCopy,letter):
                move = i
                return move

    # Corner move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = random.choice(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    # Edges move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = random.choice(edgesOpen)
        return move

def game():
    global playerOneTurn,computerTurn
    print("")
    print("")

    if playerOneTurn == True:
        while True:
            try:
                userInput = int(input("Please enter a Number(1-9) : "))
                break
            except ValueError:
                print("Please type an integer!")

        while (userInput < 1 or userInput > 9) or not(userInput in values):
            print("Incorrect number")
            print("Please try again!")
            userInput = int(input("Please enter a Number(1-9): "))

        playerOneValues.append(userInput)
        values.remove(userInput)
        board[userInput] = "X"
        playerOneTurn = False
        computerTurn = True

    elif computerTurn == True:
        computerVal = ComputerMove()
        computerValues.append(computerVal)
        values.remove(computerVal)
        board[computerVal] = "O"
        computerTurn = False
        playerOneTurn = True
        print("COMPUTER CHOSE: ",computerVal)

def isWinner(board,le):
    return((board[1] == le and board[2] == le and board[3] == le) or
           (board[4] == le and board[5] == le and board[6] == le) or
           (board[7] == le and board[8] == le and board[9] == le) or
           (board[1] == le and board[4] == le and board[7] == le) or
           (board[2] == le and board[5] == le and board[8] == le) or
           (board[3] == le and board[6] == le and board[9] == le) or
           (board[1] == le and board[5] == le and board[9] == le) or
           (board[3] == le and board[5] == le and board[7] == le))

def continueGame():
    global playerOneWin,computerWin,board,playerOneValues,computerValues,values,ticTacToe
    print()
    playAgain = input("Do you want to play again? [Y/N]: ")
    if playAgain == "N" or playAgain == "n" :
        print("\n")
        print("RESULT: ")
        print(playerOneName,"WON: ",playerOneWin)
        print(playerTwoName,"WON: ",playerTwoWin)
        ticTacToe = False
    elif playAgain == "Y" or playAgain == "y":
        board = [' ' for x in range(10)]
        playerOneValues = []
        playerTwoValues = []
        values = [1,2,3,4,5,6,7,8,9]
        playerOneTurn = False
        playerTwoTurn = False

def main():
    global board,playerOneValues,computerValues,values,playerOneTurn,computerTurn,playerOneWin,computerWin,ticTacToe
    introduction()
    print()
    startGame()
    print()
    while ticTacToe == True:
        menu()
        printBoard(board)
        game()
        if isWinner(board,"X"):
            print(playerOneName,"WON! ")
            playerOneWin += 1
            continueGame()
        elif isWinner(board,"O"):
            print("COMPUTER WON!")
            computerWin += 1
            continueGame()

        if len(values) == 0:
            print("It is a draw!")
            continueGame()


if __name__ == "__main__":
    main()
