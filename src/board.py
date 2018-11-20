import random

class Board:
    def __init__(self, n):
        self.queens = dict()
        self.columns = list()
        self.initializeBoard(n)



    def initializeBoard(self, n):
        # Subtract 1 from n to account for index starting at 0
        for x in range(n):
            columnTiles = list()

            #Generate placeholder values for the column tiles
            for k in range(n):
                columnTiles.append(k)

            #Generate a random position within a column for place a queen, update the Queen dictionary
            queenPosition = random.randint(0,n-1)
            self.queens["Q" + str(x+1)] = queenPosition

            #At this point, we should have a column list of all the columns and its values, and a queens dictionary to keep track of where the queens are placed within a column
            self.columns.append(columnTiles)


    def checkConflicts(self):
        
        conflicts= 0;
        
        #loop through index of colums for possible placements of queen
        
    #def moveQueen(self):
        
        
    #def printBoard(self):
    # print()

    
        
        
        



