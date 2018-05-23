def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        fre = {}
        max_fre = 0
        for el in words:
            if el not in fre:
                fre[el] = 0
            fre[el] += 1
            max_fre = max(max_fre, fre[el])
            
        bucket = [ [] for i in range(max_fre) ]
        for el in fre:
            bucket[fre[el]-1].append(el)
            
        re = []
        for i in range(max_fre):
            re += sorted(bucket[-i-1])
            if len(re) >= k:
                break
                
        return re[:k]