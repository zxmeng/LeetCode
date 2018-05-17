def validate(placed, n):
    if n in placed:
        return False
    
    cur = len(placed)
    for i in range(cur):
        if abs(placed[i] - n) == abs(i - cur):
            return False
    return True

def placeQueen(placed, n):
    if len(placed) == n:
        return [placed], True
    
    re = []
    found = False
    for i in range(1, n+1):
        if validate(placed, i):
            temp, flag = placeQueen(placed + [i], n)
            if flag:
                found = True
                re += temp
    
    return re, found

def nQueens(n):
    re = []
    for j in range(1, n+1):
        temp, flag = placeQueen([j], n)
        if flag:
            re += temp

    return sorted(re)

