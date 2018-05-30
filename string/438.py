def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if not p:
            return range(len(s))
        
        if len(p) > len(s):
            return []
        
        fre = {}
        for el in p:
            if el not in fre:
                fre[el] = 0
            fre[el] += 1
           
        re = []
        count = len(p)
        for i in range(len(p)):
            if s[i] in fre:
                fre[s[i]] -= 1
                if fre[s[i]] >= 0:
                    count -= 1
        if count == 0:
            re.append(0)
            
        for i in range(len(p), len(s)):
            if s[i] in fre:
                fre[s[i]] -= 1
                if fre[s[i]] >= 0:
                    count -= 1
            if s[i-len(p)] in fre:
                fre[s[i-len(p)]] += 1
                if fre[s[i-len(p)]] > 0:
                    count += 1
            if count == 0:
                re.append(i-len(p)+1)
                
        return re