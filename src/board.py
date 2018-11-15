import random

class Board:
    def __init__(self, n):
        self.queens = dict()
        self.columns = list()
        self.initializeBoard(n)

    def initializeBoard(self, n):
        # Subtract 1 from n to account for index starting at 0
        for x in range(n-1):
            columnTiles = list()
            for k in range(n):
                columnTiles.append(k)

            # Add 1 to n because randint's parameter for upper bound is not inclusive
            columnTiles[random.randint(0,n)] = "Q"

            self.columns.append(columnTiles)


