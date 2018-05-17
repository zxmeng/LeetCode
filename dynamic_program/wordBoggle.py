import copy

def findWord(board, word, i, j):
    if word == "":
        return True
    
    for k in [0, 1, -1]:
        for t in [0, 1, -1]:
            if not (k == 0 and t == 0):
                if 0 <= i+k < len(board) and 0 <= j+t < len(board[0]) and board[i+k][j+t] == word[0:1]:
                    temp = copy.deepcopy(board)
                    temp[i+k][j+t] = "_"
                    if findWord(temp, word[1:], i+k, j+t):
                        return True
                    
    return False

def wordBoggle(board, words):
    if not words:
        return words
    
    re = set()
    for word in words:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0:1]:
                    temp = copy.deepcopy(board)
                    temp[i][j] = "_"
                    if findWord(temp, word[1:], i, j):
                        re.add(word)
                        
    return sorted(list(re))
                

