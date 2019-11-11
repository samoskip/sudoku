'''
    Created on Novemeber 9th
    @author: Samuel Skipper
'''
import hashlib
def _isdone(parms):
    
    GRIDERROR = {'status':'error: invalid grid'}
    SOLVED = {'status':'solved'}
    INCOMPLETE = {'status':'incomplete'}
    WARNING = {'status':'warning'}
    INVALIDLENGTH = {'status': 'error: invalid board length'}
    INTEGRITYERROR = {'status':'error: integrity mismatch'}

    subSet = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 6, 6, 6, 7, 7, 7, 8, 8, 8, 6, 6, 6, 7, 7, 7, 8, 8, 8]
    
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
                return GRIDERROR

    if (returnIntegrity(parms, grid) == False):
        return INTEGRITYERROR

    for x in range(1, 10):
        for y in range (1, 10):
            gridPlacement = (9 * (x - 1)) + ((y - 1))
            for i in range(len(grid)):
                if (abs(grid[gridPlacement]) == abs(grid[i])) and (i != gridPlacement) and (subSet[gridPlacement] == subSet[i]) and (grid[gridPlacement] != 0):
                    return WARNING
                elif (int(i / 9) == int(gridPlacement / 9)) and (abs(grid[gridPlacement]) == abs(grid[i])) and (i != gridPlacement) and (grid[gridPlacement] != 0):
                    return WARNING

            #Vertical Search
            gridVerticalSearch = gridPlacement
            while (gridVerticalSearch < 81):
                if (abs(grid[gridVerticalSearch]) == abs(grid[gridPlacement])) and (gridVerticalSearch != gridPlacement) and (grid[gridVerticalSearch]) != 0:
                    return WARNING
                gridVerticalSearch = gridVerticalSearch + 9
            gridVerticalSearch = gridPlacement
            while (gridVerticalSearch > -1):
                if (abs(grid[gridVerticalSearch]) == abs(grid[gridPlacement])) and (gridVerticalSearch != gridPlacement) and (grid[gridVerticalSearch]) != 0:
                    return WARNING
                gridVerticalSearch = gridVerticalSearch - 9   
                
    for index in range(len(grid)):
        if grid[index] == 0:
            return INCOMPLETE
    
    return SOLVED

def returnIntegrity(parms, gridIn):
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
    if (integrityChecked != integrity):
        return False
    return True