
import game


#Given a binary matrix, rotate it
def rotatePiece(matrix):

    n=len(matrix)
    newMatrix=[0]*len(matrix)

    for a in range(n):
        newMatrix[a]= [0]*n


    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            #print("i="+str(i)+"j="+str(j))
            #print(len(matrix)-1-i)
            newMatrix[j][len(matrix)-1-i]= matrix[i][j]


    return newMatrix

def widthOfPiece(matrix):

    maxWidth = 0
    counter = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            counter+=1
        maxWidth=max(maxWidth,counter)
        counter = 0 #reset counter to 0

    return maxWidth


#print(rotatePiece(game.PIECE1))
#print(widthOfPiece(game.PIECE1))