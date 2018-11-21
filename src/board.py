import random
import timeit
class Board:
    def __init__(self, n):
        self.queens = dict()
        self.columns = list()
        self.initializeBoard(n)
        self.Max = n - 1

    def initializeBoard(self, n):
        for x in range(n):
            columnTiles = list()

            #Generate placeholder values for the column tiles
            for k in range(n):
                columnTiles.append(k)

            #Generate a random position within a column for place a queen, update the Queen dictionary
            queenPosition = random.randint(0,n-1)
            self.queens["Q" + str(x)] = queenPosition

            #At this point, we should have a column list of all the columns and its values, and a queens dictionary to keep track of where the queens are placed within a column
            self.columns.append(columnTiles)

    def updateConflicts(self):

        start = timeit.default_timer()
        colCounter = 0
        for col in self.columns:
            self.checkConflicts(col, colCounter)
            colCounter += 1;


        stop = timeit.default_timer()

        print('Time: ', stop - start)

    def checkConflicts(self, col, colCount):
        y = colCount;  #Where we are in the columns
        for position in col:
            self.columns[colCount][position] = 0
            nextTile = position

            #columns is the integer that tells us where we are in self.columns
            #This For loop checks for Diagonal Upper Right Corner
            for columns in range(y, self.Max + 1):
                columns += 1
                nextTile -= 1
                if(nextTile < 0 or columns > self.Max):
                    break

                if self.queens["Q" + str(columns)] == nextTile:
                    self.columns[colCount][position] += 1

            nextTile = position
            # This For loop checks for Diagonal Bottom Right Corner
            for columns in range(y, self.Max + 1):
                columns += 1
                nextTile += 1
                if (nextTile > self.Max) or (columns > self.Max):
                    break

                if self.queens["Q" + str(columns)] == nextTile:
                    self.columns[colCount][position] += 1

            nextTile = position
            # This For loop checks for Diagonal Upper Left Corner
            for columns in range(y, -1, -1):
                columns -= 1
                nextTile -= 1
                if (nextTile < 0) or (columns < 0):
                    break
                if self.queens["Q" + str(columns)] == nextTile:
                    self.columns[colCount][position] += 1

            nextTile = position
            # This For loop checks for Diagonal Bottom Left Corner
            for columns in range(y, -1, -1):
                columns -= 1
                nextTile += 1
                if (nextTile > self.Max) or (columns < 0):
                    break
                if self.queens["Q" + str(columns)] == nextTile:
                    self.columns[colCount][position] += 1

            # This For loop checks for Horizontal
            for columns in range(0, self.Max + 1):
                print(columns)
                if columns != colCount:
                    if self.queens["Q" + str(columns)] == position:
                        self.columns[colCount][position] += 1
            #Check Diagonal





        



