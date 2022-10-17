def solution(x, y):
    yo = 1
    for vertical in range(y-1):
        yo = yo + (vertical+1)
    
    id_ = [yo]
    for horizontal in range(x-1):
        id_.append(y+(horizontal+1))
    
    id_ = sum(id_)
    
    return str(id_)