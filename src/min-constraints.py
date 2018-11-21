from board import Board

def main():
    n = int(input("How many Queens?"))
    chessBoard = Board(n)
    #chessBoard.queens = {'Q0': 6, 'Q1': 0, 'Q2': 3, 'Q3': 5, 'Q4': 3, 'Q5': 4, 'Q6': 4, 'Q7': 2}
    print(chessBoard.queens)

    chessBoard.updateConflicts()
    print(chessBoard.columns)



if __name__ == '__main__':
    main()




