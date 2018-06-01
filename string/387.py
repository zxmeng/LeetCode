def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    fre = {}
    
    for i in range(len(s)):
        el = s[i]
        if el not in fre:
            fre[el] = []
        fre[el].append(i)
        
    first = len(s)
    flag = False
    for el in fre:
        if len(fre[el]) == 1 and fre[el][0] < first:
            first = fre[el][0]
            flag = True
    
    if not flag:
        return -1
    
    return first