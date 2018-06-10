def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
                
        return False

def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        if n == 0:
            return False
        
        for i in range(m):
            if target < matrix[i][0]:
                return False
            
            left = 0
            right = n - 1
            while left <= right:
                mid = int((left+right)/2)
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return False         
        