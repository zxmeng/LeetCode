    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        
        start = 0
        end = 0
        char = ""
        index = []
        
        for i in range(len(S)):
            if S[i:i+1] != char:
                if end - start >= 2:
                    index.append([start, end])
                char = S[i:i+1]
                start = i
            end = i
        
        if end - start >= 2:
            index.append([start, end])
            
        return index