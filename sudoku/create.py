def _create(parms):
    #result = {'status': 'create stub'}
    if (not ("level" in parms)):
        result = {'status': 'create stub'}
    else:
        result = int(parms["level"])
        if (result == 1):
            levelReturn = "This is level one"
        elif (result == 2):
            levelReturn = "This is level two"
        elif (result == 3):
            levelReturn = "This is level three"
        elif (result == 4):
            levelReturn = "This is level four"
        elif (result == 5):
            levelReturn = "This is level five"
        elif (result > 5) or (result < 1):
            levelReturn = "{'status':'error: invalid level'}"

        
    return levelReturn
