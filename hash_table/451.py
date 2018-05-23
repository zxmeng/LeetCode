def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        fre = {}
        max_fre = 0
        for el in s:
            if el not in fre:
                fre[el] = 0
            fre[el] += 1
            max_fre = max(max_fre, fre[el])
            
        bucket = [[] for i in range(max_fre)]
        for el in fre:
            bucket[fre[el]-1].append(el)
        
        re = []
        for i in range(max_fre):
            for el in bucket[-i-1]:
                re.append( el * (max_fre - i) )
                
        return "".join(re)