from board import Board
from copy import deepcopy
import timeit
import time

def minConstraints(csp, maxSteps):
    steps = 0
    for x in range(csp.Max + 1):
        csp.updateConflicts(x)

    columns = (csp.columns)
    for x in range(maxSteps):
        if csp.checkSolution() == 1:
            return csp
        steps += 1

        var = csp.chooseQueen()
        old = csp.queens["Q" + str(var)]
        #col = csp.columns[var]
        newIndex = csp.minIndex(var)
        csp.queens["Q" + str(var)] = newIndex
    return 0

def main():

    #get user input from console
    n = int(input("How many Queens?"))
    chessBoard = Board(n)

    #incase we ever need to manually input a board use below
    #chessBoard.queens = {'Q0': 0, 'Q1': 2, 'Q2': 3, 'Q3': 1}

    #Call the solver and pass the board to minconstraints
    #the max size here will be n*2 , if reached the program
    #will restart
    start = time.time() #start measuring execution time
    solution = 0
    while solution == 0:
        solution = minConstraints(chessBoard, 100000)



    print(chessBoard.queens)
    print("Solution Found")

    #end of execution time for solver
    end = time.time()
    print("It took {} seconds".format(end-start))

    #write the output to a text file in a readable format
    with open('out.txt', 'w') as f:
        for col in range(n):
            for row in range(n):
                if (col == chessBoard.queens["Q" + str(row)]):
                    f.write("Q|")
                else:
                    f.write("X|")
            f.write("\n")
    f.close()



if __name__ == '__main__':
    main()




