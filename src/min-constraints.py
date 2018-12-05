from board import Board
from copy import deepcopy
import timeit
import time

def minConstraints(csp, maxSteps):
    steps = 0
    #current = deepcopy(csp)
    for x in range(maxSteps):
        print("We are on step ", steps)

        startSol = time.time()
        if csp.checkSolution() == 1:
            print("It took {} steps".format(steps))
            return csp
        endSol = time.time()
        print("Checking if current board took {} seconds".format(endSol - startSol))

        startQueen = time.time()
        var = csp.chooseQueen()
        endQueen = time.time()
        print("Choose queen took {} seconds".format(endQueen - startQueen))

        startIndex = time.time()
        newIndex = csp.minIndex(var)
        endIndex = time.time()
        print("Finding the new spot took {} seconds".format(endIndex - startIndex))

        #print("Q{} was moved to tile {}.".format(var,newIndex))

        startMove = time.time()
        csp.queens["Q" + str(var)] = newIndex
        endMove = time.time()
        print("Moving the queen took {} seconds".format(endMove - startMove))

        startUpdate = time.time()
        csp.updateConflicts()
        endUpdate = time.time()
        print("Updating took {} seconds".format(endUpdate - startUpdate))

        steps += 1

    print("It took {} steps".format(steps))
    return 0

def main():
    start = time.time()
    n = int(input("How many Queens?"))

    chessBoard = Board(n)
    #chessBoard.queens = {'Q0': 0, 'Q1': 1, 'Q2': 3, 'Q3': 1}

    #print(chessBoard.queens)


    chessBoard.updateConflicts()
    solution = minConstraints(chessBoard, 250)
    #chessBoard.updateConflicts()

    if solution == 0:
        print("A solution was not found.")
    else:
        print("WE FUCKING GOT IT MATE")
    end = time.time()

    print("It took {} seconds".format(end-start))

    print(chessBoard.queens)
    print(chessBoard.columns)



if __name__ == '__main__':
    main()




