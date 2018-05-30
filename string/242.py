def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        fre = {}
        for el in s:
            if el not in fre:
                fre[el] = 0
            fre[el] += 1
            
        
        for el in t:
            if el not in fre:
                return False
            fre[el] -= 1
            if fre[el] == 0:
                del fre[el]
                
        return not fre