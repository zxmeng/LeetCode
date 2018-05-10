def isCryptSolution(crypt, solution):
    dict = {}
    
    for i in range(len(solution)):
        dict[solution[i][0]] = solution[i][1]

    if (int(dict[crypt[0][0:1]]) == 0 and len(crypt[0]) > 1) or (int(dict[crypt[1][0:1]]) == 0 and len(crypt[1]) > 1) or (int(dict[crypt[2][0:1]]) == 0 and len(crypt[2]) > 1):
        return False
    
    for el in dict:
        crypt[0] = crypt[0].replace(el, dict[el])
        crypt[1] = crypt[1].replace(el, dict[el])
        crypt[2] = crypt[2].replace(el, dict[el])
        
    return int(crypt[2]) == int(crypt[0]) + int(crypt[1])