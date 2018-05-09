def firstNotRepeatingCharacter(s):
    index = [0] * 26
    
    for i in range(len(s)):
        temp = ord(s[i:i+1]) - ord('a')
        if index[temp] > 0:
            index[temp] *= -1
        elif index[temp] == 0:
            index[temp] = i+1
            
    char = '_'
    min = len(s)+1
    for i in range(26):
        if index[i] > 0 and index[i] < min:
            min = index[i]
            char = chr(i + ord('a'))
            
    return char