from board import Board
from copy import deepcopy

def minConstraints(csp, maxSteps):
    current = deepcopy(csp)
    for x in range(maxSteps):
        if csp.checkSolution() == 1:
            return csp

        var = csp.chooseQueen()
        newIndex = csp.minIndex(var)
        print("Q{} was moved to tile {}.".format(var,newIndex))
        csp.queens["Q" + str(var)] = newIndex
        csp.updateConflicts()
    return 0

def main():
    n = int(input("How many Queens?"))
    chessBoard = Board(n)
    #chessBoard.queens = {'Q0': 0, 'Q1': 1, 'Q2': 3, 'Q3': 1}

    #print(chessBoard.queens)


    chessBoard.updateConflicts()
    minConstraints(chessBoard, 1000)
    #chessBoard.updateConflicts()
    solution = chessBoard.checkSolution()

    if solution == 0:
        print("A solution was not found.")
    else:
        print("WE FUCKING GOT IT MATE")



    print(chessBoard.queens)
    print(chessBoard.columns)



if __name__ == '__main__':
    main()




