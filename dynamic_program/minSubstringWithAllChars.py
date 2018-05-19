def minSubstringWithAllChars(s, t):
    if not s or not t:
        return ""
    
    re = ""
    min_len = len(s)
    temp = set(t)
    start = 0
    for i in range(len(s)):
        temp -= set(s[i])
        while i - start + 1 > len(t):
            if s[start] not in t or s[start] in s[start+1:i+1]:
                start += 1
            else:
                break
        if not temp:
            if min_len > i - start:
                min_len = i - start
                re = s[start:i+1]
            
    return re


def minSubstringWithAllChars2(s, t):
    if not s or not t:
        return ""
    
    ind = max([ s.find(el) for el in t ])
    start = 0
    re = ""
    min_len = len(s)
    for i in range(ind, len(s)):
        while i - start + 1 > len(t):
            if s[start] not in t or s[start] in s[start+1:i+1]:
                start += 1
            else:
                break
        if min_len > i - start:
            min_len = i - start
            re = s[start:i+1]
            
    return re


