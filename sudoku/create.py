def _create(parms):
    #result = {'status': 'create stub'}
    if (not ("level" in parms)):
        result = {'status': 'create stub'}
    else:
        result = parms["level"]
        if (result == 1):
            levelReturn = "This is level one"
        elif (result == 2):
            levelReturn = "This is level two"
        elif (result == 3):
            levelReturn = "This is level three"

        
    return levelReturn
