import hashlib

def _insert(parms):
    
    #Errors to be called
    GRIDERROR = {'status':'error: invalid grid'}
    CELLERROR = {'status':'error: invalid cell reference'}
    VALUEERROR = {'status':'error: invalid value'}
    INTEGRITYERROR = {'status':'error: integrity mismatch'}
    FIXEDERROR = {'status':'error: attempt to change fixed hint'}
    MISSINGCELLERROR = {'status':'error: missing cell reference'}
    STATUS = 'ok'
    
    subSet = [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 6, 6, 6, 7, 7, 7, 8, 8, 8, 6, 6, 6, 7, 7, 7, 8, 8, 8]
    
    #cell
    if "cell" in parms:
        cell = parms["cell"]
    else:
        return MISSINGCELLERROR
    
    if (cell[0].lower() == 'r') and (cell[2].lower() == 'c') and (int(cell[1]) > 0) and (int(cell[3]) > 0):
        row = int(cell[1])
        column = int(cell[3])
    else:
        return CELLERROR

    #value
    if "value" in parms:
        value = parms["value"]
    else:
        value = 0
    if (value.isdigit() == False) or (int(value) > 9 or int(value) < 0):
        return VALUEERROR
    
    
    #grid
    if "grid" in parms:
        grid = list(parms["grid"].split(","))
        grid[0] = str(grid[0])[1:]
        grid[80] = str(grid[80])[:-1]
        gridPlacement = (9 * (row - 1)) + ((column - 1))
        for i in range(len(grid)):
            try:
                int(grid[i])
                for i in range(len(grid)):
                    grid[i] = int(grid[i])
            except ValueError:
                return GRIDERROR

    #integrity
    integrity = parms["integrity"]
    stringHash = ""
    dictList = [None] * 81
    counter = 0
    for index in grid:
        if (counter == 0 or counter == 80):
            dictList[counter] = index
        else:
            dictList[(counter * 9) % 80] = index
        counter = counter + 1
    for index in range(len(dictList)):
        stringHash = stringHash + str(dictList[index])

    integrityChecked = hashlib.sha256(stringHash.encode('utf-8')).hexdigest()    
    if (integrityChecked != integrity):
        return INTEGRITYERROR

    if (int(grid[gridPlacement]) > -1):
        grid[gridPlacement] = int(value)
    else:
        return FIXEDERROR
    
    #Grid Search and Horizontal Search
    for i in range(len(grid)):
        if (abs(grid[gridPlacement]) == abs(grid[i])) and (i != gridPlacement) and (subSet[gridPlacement] == subSet[i]):
            STATUS = 'warning'
        elif (int(i / 9) == int(gridPlacement / 9)) and (abs(grid[gridPlacement]) == abs(grid[i])) and (i != gridPlacement):
            STATUS = 'warning'
    
    #Vertical Search
    gridVerticalSearch = gridPlacement + 9
    while (gridVerticalSearch < 81):
        if (grid[gridVerticalSearch] == grid[gridPlacement]):
            STATUS = 'warning'
        gridVerticalSearch = gridVerticalSearch + 9
    gridVerticalSearch = gridPlacement - 9
    while (gridVerticalSearch > -1):
        if (grid[gridVerticalSearch] == grid[gridPlacement]):
            STATUS = 'warning'
        gridVerticalSearch = gridVerticalSearch - 9
            
    return { 'grid' : grid,
            'integrity' : integrity,
            'status' : STATUS
        }