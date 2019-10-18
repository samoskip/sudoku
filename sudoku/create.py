def _create(parms):
    #result = {'status': 'create stub'}
    if (not ("level" in parms)):
        result = {'status': 'create stub'}
    else:
        result = parms["level"]
        
    return result
