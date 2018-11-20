from board import Board

def main():
    n = int(input("How many Queens?"))
    chessBoard = Board(n)
    print(chessBoard.queens)
    print(chessBoard.columns)
    chessBoard.checkConflicts()



if __name__ == '__main__':
    main()




