def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        num = 0
        for i in range(n):
            num += (ord(s[i]) - ord("A") + 1) * (26 ** (n-1-i))
            
        return num