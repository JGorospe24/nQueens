import random

class Board:
    def __init__(self, n):
        self.queens = dict()
        self.columns = list()
        self.initializeBoard(n)
        self.Max = 0



    def initializeBoard(self, n):
        # Subtract 1 from n to account for index starting at 0
        self.Max = n -1

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

    def checkConflictsHorizontal(self):
        col = 0
        #Get a new list of constraints, representing the next column
        for conflicts in self.columns:
            row = 0
            #Iterate through each row in this column
            for x in conflicts:
                tempConflicts = 0

                #Check every column for queen in current row
                for y in self.queens:
                    print("Checking row {} in {} for spot {} in list {}".format(row, y, x, conflicts))
                    if self.queens[y] == row:
                        tempConflicts += 1
                #Check if queen in current column list is in the row we are checking, since it will count itself as a conflict in this case
                if self.queens["Q" + str(col+1)] == row:
                    tempConflicts -= 1
                #Update the conflicts list for that particular block in the column
                conflicts[x] = tempConflicts
                
                row += 1
            col += 1

    def checkConflictsRightDown(self):
        col = 0

        for conflicts in self.columns:

            for x in range(len(conflicts)):
                tempConflicts = 0
                # print("x is: {}, conflicts is: {}".format(x, conflicts))
                row = x + 1

                for y in self.queens:
                    if int(y[1]) - 1 > col:
                        # print("Checking {}R:{} for {}R:{}".format(y, row, "Q" + str(col+1), x))
                        if self.queens[y] == row:
                            tempConflicts += 1
                            # print("TEMPCONF+, current: {}".format(tempConflicts))

                        row += 1

                conflicts[x] = conflicts[x] + tempConflicts
            col += 1

    def checkConflictsRightUp(self):
        col = 0

        for conflicts in self.columns:

            for x in range(len(conflicts)):
                tempConflicts = 0

                row = x - 1
                for y in self.queens:
                    if int(y[1]) - 1 > col:
                        if self.queens[y] == row:
                            tempConflicts += 1
                        row -= 1

                conflicts[x] = conflicts[x] + tempConflicts
            col += 1

    def checkConflictsLeftUp(self):
        col = 0

        for conflicts in self.columns:

            for x in range(len(conflicts)):
                tempConflicts = 0

                row = x - col
                for y in self.queens:
                    if int(y[1]) - 1 < col:
                        if self.queens[y] == row:
                            tempConflicts += 1
                        row += 1

                conflicts[x] = conflicts[x] + tempConflicts
            col += 1

    def checkConflictsLeftDown(self):
        col = 0

        for conflicts in self.columns:

            for x in range(len(conflicts)):
                tempConflicts = 0

                row = x + col
                for y in self.queens:
                    if int(y[1]) - 1 < col:
                        if self.queens[y] == row:
                            tempConflicts += 1
                        row -= 1

                conflicts[x] = conflicts[x] + tempConflicts
            col += 1


    def checkConflicts(self):
        
        conflicts= 0;
        self.checkConflictsHorizontal()
        print("After Horizontal checks: ", end='')
        print(self.columns)
        self.checkConflictsRightDown()
        print("After Down Right checks: ", end='')
        print(self.columns)
        self.checkConflictsRightUp()
        print("After Up Right checks:    ", end='')
        print(self.columns)
        self.checkConflictsLeftUp()
        print("After Left Up checks:    ", end='')
        print(self.columns)
        self.checkConflictsLeftDown()
        print("After Left Down checks:    ", end='')
        print(self.columns)

        #loop through index of colums for possible placements of queen
        
    #def moveQueen(self):
        
        
    #def printBoard(self):
    # print()

    
        
        
        



