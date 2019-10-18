def _create(parms):
    #result = {'status': 'create stub'}
    if (not ("level" in parms)):
        result = {'status': 'create stub'}
    else:
        result = parms["level"]      
        levelNum = int(result)
        
        if (levelNum == 1):
            levelReturn = "This is level one"
        elif (levelNum == 2):
            levelReturn = "This is level two"
        elif (levelNum == 3 or result == ""):
            levelReturn = "This is level three"
        elif (levelNum == 4):
            levelReturn = "This is level four"
        elif (levelNum == 5):
            levelReturn = "This is level five"
        elif (levelNum > 5) or (result < 1):
            levelReturn = "{'status':'error: invalid level'}"


        
    return levelReturn
