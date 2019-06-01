
import random

#Constants
BOARDWIDTH = 10
BOARDHEIGHT = 20

#Shapes- 7 in total
PIECE1= ([1,1],[1,1])  #SquarePiece
PIECE2= ([1,0,0],[1,1,0],[0,1,0])   #S piece
PIECE3= ([1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0])   #I Piece
PIECE4= ([0,1,0],[1,1,1],[0,0,0]) #T Piece
PIECE5= ([1,0,0],[1,1,1],[0,0,0]) #Backwards L Piece
PIECE6= ([1,1,0],[0,1,1],[0,0,0]) #Z Piece
PIECE7= ([0,0,1],[1,1,1],[0,0,0]) #L Piece

#ARRAY OF THE PIECES.
PIECES=[0,0,0,0,0,0,0]
PIECES[0]=PIECE1
PIECES[1]=PIECE2
PIECES[2]=PIECE3
PIECES[3]=PIECE4
PIECES[4]=PIECE5
PIECES[5]=PIECE6
PIECES[6]=PIECE7


#Boolean Variables for continuation of game
continuation = True

def createBoard(width, height):

    gameBoard = [0] * height

    for a in range(height):
        gameBoard[a] = [0] * width

    return gameBoard


#Mainly for Debugging
def printBoard(board):

    for i in range(len(board)):
        print(board[i])

#Returns nothing after having checked all the rows that are full/ filled with 1's.
#With these full rows, they are deleted. New rows of 0 are placed up top.
def checkCompleteRow(board):

    checked=True
    counter = 0
    width=len(board[0])
    height = len(board)

    #printBoard(board)
    #print("initial")

    for a in range(len(board)-1,-1,-1):
        for b in range(len(board[a])):
            if (board[a][b]==1):
                counter +=1

        if (counter == width):
            #print(board[a])
            del board[a]

        counter = 0

    #print(len(board))


    for c in range(height-len(board)):
        board.insert(c,[0] * width)

    #printBoard(board)
    #print(len(board))

#Generates a random piece. Should be an equal distribution over long term/ expected value.
def generatePiece():

    randomNumber = random.randint(0,6)
    return PIECES[randomNumber]



# def dropPiece(column,piece,board):


#def gamePlay(gameBoard):

 #   while (continuation):
  #      generatePiece()




mainBoard = createBoard(BOARDWIDTH,BOARDHEIGHT)
mainBoard[3]=[1,1,1,1,1,1,1,1,1,1]
mainBoard[4]=[1,1,1,1,1,1,1,1,1,1]
mainBoard[5]=[0,1,1,1,1,1,1,1,1,1]

#printBoard(mainBoard)

checkCompleteRow(mainBoard)
printBoard(mainBoard)
print(len(mainBoard))
