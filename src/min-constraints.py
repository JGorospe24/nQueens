from board import Board
from copy import deepcopy

def minConstraints(csp, maxSteps):
    current = deepcopy(csp)
    for x in range(maxSteps):
        if current.checkSolution() == 1:
            return current

        var = current.chooseQueen()
        newIndex = current.minIndex(var)
        print(var,newIndex)
        current.queens["Q" + str(var)] = newIndex
        current.updateConflicts()
    return 0

def main():
    n = int(input("How many Queens?"))
    chessBoard = Board(n)
    chessBoard.queens = {'Q0': 0, 'Q1': 1, 'Q2': 3, 'Q3': 1}

    #print(chessBoard.queens)


    chessBoard.updateConflicts()
    minConstraints(chessBoard, 1000)
    print(chessBoard.checkSolution())

    #print(chessBoard.queens)
    print(chessBoard.columns)



if __name__ == '__main__':
    main()




