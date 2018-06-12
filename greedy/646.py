def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
        pairs.sort(key=lambda pair: pair[1])
        last = pairs[0][1]
        count = 1
        
        for i in range(1, len(pairs)):
            if pairs[i][0] > last:
                count += 1
                last = pairs[i][1]
                
        return count