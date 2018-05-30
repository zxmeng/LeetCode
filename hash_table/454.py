def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        ab = {}
        cd = {}
        
        for a in A:
            for b in B:
                if a+b not in ab:
                    ab[a+b] = 0
                ab[a+b] += 1
                
        for c in C:
            for d in D:
                if c+d not in cd:
                    cd[c+d] = 0
                cd[c+d] += 1
           
        re = 0
        for el in ab:
           if -el in cd:
            re += ab[el] * cd[-el]
            
        return re