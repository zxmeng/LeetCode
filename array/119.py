def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]
        
        re = [1,1]
        for i in range(2, rowIndex+1):
            temp = [1]
            for j in range(len(re)-1):
                temp.append(re[j]+re[j+1])
            temp.append(1)
            re = temp
            
        return re