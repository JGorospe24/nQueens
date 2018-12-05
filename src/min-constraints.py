from board import Board
from copy import deepcopy
import timeit
import time


def minConstraints(csp, maxSteps):
    steps = 0
    for x in range(maxSteps):

        print("We are on step ", steps)

        if csp.checkSolution() == 1:
            print("It took {} steps".format(steps))
            return csp
        steps += 1
        var = csp.chooseQueen()
        csp.updateConflicts(var)
        newIndex = csp.minIndex(var)
        csp.queens["Q" + str(var)] = newIndex

    print("It took {} steps".format(steps))
    return 0

def main():
    start = time.time() #start measuring execution time

    #get user input from consol
    n = int(input("How many Queens?"))

    chessBoard = Board(n)

    #incase we ever need to manually input a board use below
    #chessBoard.queens = {'Q0': 0, 'Q1': 1, 'Q2': 3, 'Q3': 1}

    #Call the solver and pass the board to minconstraints
    #the max size here will be n*2 , if reached the program
    #will restart
    solution = 0
    while solution == 0:
        chessBoard.updateConflictsInitial()
        solution = minConstraints(chessBoard, n*2)

    print("Solution Found")

    #end of execution time for solver
    end = time.time()
    print("It took {} seconds".format(end-start))

    #write the output to a text file in a readable format
    with open('out.txt', 'w') as f:
        for row in range(n):
            for col in chessBoard.columns:
                f.write("{}|".format(col[row]))
            f.write("\n")
    f.close()



if __name__ == '__main__':
    main()




