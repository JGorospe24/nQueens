import random
import timeit
class Board:
    def __init__(self, n):
        self.Max = n - 1
        self.queens = dict()
        self.columns = list()
        self.initializeBoard(n)
        self.placeQueens(n)
        self.unresolved = list()


    def initializeBoard(self, n):
        for x in range(n):
            columnTiles = list()

            #Generate placeholder values for the column tiles
            for k in range(n):
                columnTiles.append(0)

            #Generate a random position within a column for place a queen, update the Queen dictionary
            self.queens["Q" + str(x)] = -1

            #At this point, we should have a column list of all the columns and its values, and a queens dictionary to keep track of where the queens are placed within a column
            self.columns.append(columnTiles)



    def placeQueens(self, n):
        for x in range(n):
            self.updateConflicts(x)
            minVal = min(self.columns[x])


            if(self.columns[x].count(minVal) > 1):
                minPositions = [(i,j) for i,j in enumerate(self.columns[x]) if j == minVal]
                randIndex = random.randint(0, len( minPositions) - 1)
                queenPos = minPositions[randIndex][0]
            else:
                queenPos = self.columns[x].index(minVal)



            self.queens["Q" + str(x)] = queenPos

        return











    def updateConflicts(self, index):
        self.checkConflicts(self.columns[index], index)

    def updateConflictsAllQueens(self):
        for col in range(len(self.columns)):
            self.checkNeighbours(self.queens["Q" + str(col)], col)

    def checkSolution(self):
        counter = 0
        self.updateConflictsAllQueens()
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

            self.updateConflicts(index)


            z = self.columns[index]
            self.checkNeighbours(qIndex, index)

            conflicts = self.columns[index][qIndex]
            #Check if that spot is 0
            f = self.queens
            m = self.columns[index]
            h = self.columns[index].count(conflicts)
            l = min(self.columns[index])
            c = self.columns[index].count(l)

            if conflicts != l:
                return index
            elif self.columns[index].count(l) > 1:
                return index

    def minIndex(self, col):
        column = self.columns[col]
        minValue = min(column)
        #minList is position of minimum values in current col
        minList = list()
        #initialize it with index 0

        for i,j in enumerate(column):
            if(j == minValue):
                if i != self.queens["Q" + str(col)]:
                    minList.append(i)

        if(len(minList) > 1):
            randomInt = random.randint(0, len(minList)-1)
            return minList[randomInt]
        else:
            return minList[0]


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

    def checkNeighbours(self, queenPosition, column):
        #columns is the integer that tells us where we are in self.columns
        conflicts = 0


        qp = queenPosition - 1
        col = column + 1
        #This For loop checks for Diagonal Upper Right Corner
        for columns in range(col, self.Max + 1):
            if(qp < 0 or columns > self.Max):
                break

            if self.queens["Q" + str(columns)] == qp:
                conflicts += 1
                #print("Q{}@{}: found conflict right up for position {} in Q{}".format(columns, self.queens["Q" + str(columns)],  position, colCount))
            qp -= 1


        col = column + 1
        qp = queenPosition + 1
        # This For loop checks for Diagonal Bottom Right Corner
        for columns in range(col, self.Max + 1):
            if (qp > self.Max) or (columns > self.Max):
                break
            if self.queens["Q" + str(columns)] == qp:
                conflicts += 1
                #print("Q{}@{}: Found conflict Right Down for position {} in Q{}".format(columns, self.queens["Q" + str(columns)],  position, colCount))
            qp += 1


        col = column - 1
        qp = queenPosition - 1
        # This For loop checks for Diagonal Upper Left Corner
        for columns in range(col, -1, -1):
            if (qp < 0) or (columns < 0):
                break

            if self.queens["Q" + str(columns)] == qp:
                conflicts += 1
                #print("Q{}@{}: Found conflict left up for position {} in Q{}".format(columns, self.queens["Q" + str(columns)],  position, colCount))
            qp -= 1

        col = column - 1
        qp = queenPosition + 1
        # This For loop checks for Diagonal Bottom Left Corner
        for columns in range(col, -1, -1):
            if (qp > self.Max) or (columns < 0):
                break
            if self.queens["Q" + str(columns)] == qp:
                conflicts += 1
                #print("Q{}@{} Found conflict left down for position {} in Q{}".format(columns, self.queens["Q" + str(columns)],  position, colCount))
            qp += 1

        # This For loop checks for Horizontal
        for columns in range(0, self.Max + 1):
            if columns != column:
                if self.queens["Q" + str(columns)] == queenPosition:
                    conflicts += 1

                    #print("Q{}@{}: Found conflict Horizontal for position {} in Q{}".format(columns, self.queens["Q" + str(columns)], position, colCount))
        #Check Diagonal

        self.columns[column][queenPosition] = conflicts





        



