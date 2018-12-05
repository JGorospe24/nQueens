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

    def updateConflicts(self, index):
        self.checkConflicts(self.columns[index], index)

    def updateConflictsInitial(self):
        colCounter = 0
        for col in self.columns:
            self.checkConflicts(col, colCounter)
            colCounter += 1;

    def checkSolution(self):
        counter = 0
        for x in self.queens:
            if self.columns[counter][self.queens[x]] != 0:
                return 0
            counter += 1
        return 1

    def chooseQueen(self):
        while True:
            #Choose random column
            index = random.randint(0, self.Max)
            #Check queen
            qIndex = self.queens["Q" + str(index)]
            #Check if that spot is 0
            #print("Checking Q{} at position {}, there are {} conflicts".format(index, qIndex, self.columns[index][qIndex]))
            if self.columns[index][qIndex] != 0 or self.columns[index].count(0) > 1:
                return index

    def minIndex(self, col):
        column = self.columns[col]
        minValue = column[0]
        #minList is position of minimum values in current col
        minList = list()
        #initialize it with index 0
        minList.append(0)
        minInstances = 1

        for x in range(self.Max + 1):
            if column[x] < minValue:
                minValue = column[x]
                #if new min value found, clear old list and enter new minindex
                minList.clear()
                minList.append(x)
                minInstances = 1
            elif column[x] == minValue:
                minList.append(x)
                minInstances+=1

        randomIndex = random.randint(0, minInstances - 1)
        return minList[randomIndex]

    def checkConflicts(self, col, colCount):
        y = colCount #Where we are in the columns
        #print(self.queens)
        #print(self.columns)
        #print("THIS IS FOR COLUMN {}".format(colCount))
        for position in range(len(col)):
            #print("We are checking position ", position)
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
                    #print("Q{}@{}: found conflict right up for position {} in Q{}".format(columns, self.queens["Q" + str(columns)],  position, colCount))

            nextTile = position
            # This For loop checks for Diagonal Bottom Right Corner
            for columns in range(y, self.Max + 1):
                columns += 1
                nextTile += 1
                if (nextTile > self.Max) or (columns > self.Max):
                    break

                if self.queens["Q" + str(columns)] == nextTile:
                    self.columns[colCount][position] += 1
                    #print("Q{}@{}: Found conflict Right Down for position {} in Q{}".format(columns, self.queens["Q" + str(columns)],  position, colCount))

            nextTile = position
            # This For loop checks for Diagonal Upper Left Corner
            for columns in range(y, -1, -1):
                columns -= 1
                nextTile -= 1
                if (nextTile < 0) or (columns < 0):
                    break
                if self.queens["Q" + str(columns)] == nextTile:
                    self.columns[colCount][position] += 1
                    #print("Q{}@{}: Found conflict left up for position {} in Q{}".format(columns, self.queens["Q" + str(columns)],  position, colCount))

            nextTile = position
            # This For loop checks for Diagonal Bottom Left Corner
            for columns in range(y, -1, -1):
                columns -= 1
                nextTile += 1
                if (nextTile > self.Max) or (columns < 0):
                    break
                if self.queens["Q" + str(columns)] == nextTile:
                    self.columns[colCount][position] += 1
                    #print("Q{}@{} Found conflict left down for position {} in Q{}".format(columns, self.queens["Q" + str(columns)],  position, colCount))

            # This For loop checks for Horizontal
            for columns in range(0, self.Max + 1):
                if columns != colCount:
                    if self.queens["Q" + str(columns)] == position:
                        self.columns[colCount][position] += 1
                        #print("Q{}@{}: Found conflict Horizontal for position {} in Q{}".format(columns, self.queens["Q" + str(columns)], position, colCount))
            #Check Diagonal





        



