'''
    Created on Novemeber 9th
    @author: Samuel Skipper
'''

import hashlib

mainGrid = []
subSet = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 6, 6, 6, 7, 7, 7, 8, 8, 8, 6, 6, 6, 7, 7, 7, 8, 8, 8]


INVALIDCHAR = {'status': 'error: invalid character in grid'}
INVALIDLENGTH = {'status': 'error: invalid board length'}
INVALIDSOLUTION = {'status': 'error: board not solvable'}
INTEGRITYERROR = {'status':'error: integrity mismatch'}

def _solve(parms):
    
    global mainGrid
    if "grid" in parms:
        grid = list(parms["grid"].split(","))
        if (len(grid) != 81):
            return INVALIDLENGTH
        grid[0] = str(grid[0])[1:]
        grid[80] = str(grid[80])[:-1]
        for i in range(len(grid)):
            try:
                int(grid[i])
                for i in range(len(grid)):
                    grid[i] = int(grid[i])
            except ValueError:
                return INVALIDCHAR
    
    if ((returnIntegrity(parms, grid, True)) == False):
        return INTEGRITYERROR

    mainGrid = grid
    if (suggestSolve()):
        newIntegrity = returnIntegrity(parms, mainGrid, False)
        return {'grid': mainGrid,
                'integrity': newIntegrity,
                'status': 'ok'}
    else:
        return INVALIDSOLUTION

def returnIntegrity(parms, gridIn, returnAndCompare):
    integrity = parms["integrity"]
    stringHash = ""
    dictList = [None] * 81
    counter = 0
    for index in gridIn:
        if (counter == 0 or counter == 80):
            dictList[counter] = index
        else:
            dictList[(counter * 9) % 80] = index
        counter = counter + 1
    for index in range(len(dictList)):
        stringHash = stringHash + str(dictList[index])

    integrityChecked = hashlib.sha256(stringHash.encode('utf-8')).hexdigest()
    if (returnAndCompare) and (integrityChecked != integrity):
        return False
    else:
        return integrityChecked

def suggestSolve():
    if checkIfSolved():
        return True
    else:
        for i in range(1, 10):
            row, column = nextOpenGrid(True)
            if checkForConflicts(row, column, i):
                if suggestSolve():
                    return True
                else:
                    mainGrid[positionCorrection(row, column)] = 0
    return False

#returns index for next 0 in grid, parameters return results in plain index or row, column
def nextOpenGrid(rowColumnOrIndex):
    for indexVertical in range(1, 10):
        for indexHorizontal in range(1, 10):
            gridPlace = (9 * (indexVertical - 1)) + ((indexHorizontal - 1))
            if (mainGrid[gridPlace] == 0):
                if (rowColumnOrIndex):
                    return indexVertical, indexHorizontal
                else:
                    return gridPlace
                    

def positionCorrection(row, column):
    gridPlace = (9 * (row - 1)) + ((column - 1))
    return gridPlace

#True means no conflicts
def checkForConflicts(row, column, number):
    #global mainGrid
    gridPlacement = (9 * (row - 1)) + ((column - 1))
    numberCache = mainGrid[gridPlacement]
    mainGrid[gridPlacement] = number
    
    for i in range(len(mainGrid)):
        if (abs(mainGrid[gridPlacement]) == abs(mainGrid[i])) and (i != gridPlacement) and (subSet[gridPlacement] == subSet[i]) and (mainGrid[gridPlacement] != 0):
            mainGrid[gridPlacement] = numberCache
            return False
        elif (int(i / 9) == int(gridPlacement / 9)) and (abs(mainGrid[gridPlacement]) == abs(mainGrid[i])) and (i != gridPlacement) and (mainGrid[gridPlacement] != 0):
            mainGrid[gridPlacement] = numberCache
            return False
    
    #Vertical Search
    gridVerticalSearch = gridPlacement
    while (gridVerticalSearch < 81):
        if (abs(mainGrid[gridVerticalSearch]) == abs(mainGrid[gridPlacement])) and (gridVerticalSearch != gridPlacement):
            mainGrid[gridPlacement] = numberCache
            return False
        gridVerticalSearch = gridVerticalSearch + 9
    gridVerticalSearch = gridPlacement
    while (gridVerticalSearch > -1):
        if (abs(mainGrid[gridVerticalSearch]) == abs(mainGrid[gridPlacement])) and (gridVerticalSearch != gridPlacement):
            mainGrid[gridPlacement] = numberCache
            return False
        gridVerticalSearch = gridVerticalSearch - 9
            
    return True

def checkIfSolved():
    for x in range(1, 10):
        for y in range (1, 10):
            gridPlacement = (9 * (x - 1)) + ((y - 1))
            for i in range(len(mainGrid)):
                if mainGrid[i] == 0:
                    return False
                if (abs(mainGrid[gridPlacement]) == abs(mainGrid[i])) and (i != gridPlacement) and (subSet[gridPlacement] == subSet[i]) and (mainGrid[gridPlacement] != 0):
                    return False
                elif (int(i / 9) == int(gridPlacement / 9)) and (abs(mainGrid[gridPlacement]) == abs(mainGrid[i])) and (i != gridPlacement) and (mainGrid[gridPlacement] != 0):
                    return False

            #Vertical Search
            gridVerticalSearch = gridPlacement
            while (gridVerticalSearch < 81):
                if (abs(mainGrid[gridVerticalSearch]) == abs(mainGrid[gridPlacement])) and (gridVerticalSearch != gridPlacement):
                    return False
                gridVerticalSearch = gridVerticalSearch + 9
            gridVerticalSearch = gridPlacement
            while (gridVerticalSearch > -1):
                if (abs(mainGrid[gridVerticalSearch]) == abs(mainGrid[gridPlacement])) and (gridVerticalSearch != gridPlacement):
                    return False
                gridVerticalSearch = gridVerticalSearch - 9    
    return True