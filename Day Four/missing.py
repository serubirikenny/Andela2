def find_missing(x,y):
    if len(x) < 1 and len(y) <1:
        return 0


    if len(x) < len(y):
        x,y = y,x
    for i in x:
        if i not in y:
            return i
    return 0
