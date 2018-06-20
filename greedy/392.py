def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    start = 0
    for i in range(len(s)):
        target = s[i]
        find = False
        for j in range(start, len(t)):
            if t[j] == s[i]:
                find = True
                start = j + 1
                break
        
        if not find:
            return False

    return True