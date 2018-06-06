def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1],[1,1]]
        
        re = [[1], [1,1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(len(re[-1])-1):
                temp.append(re[-1][j]+re[-1][j+1])
            temp.append(1)
            re.append(temp)
            
        return re