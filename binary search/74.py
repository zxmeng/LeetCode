def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        ind = -1
        if target <= matrix[0][-1]:
            ind = 0
        else:
            for i in range(1, m):
                if matrix[i-1][-1] < target <= matrix[i][-1]:
                    ind = i
                    break
                    
        left = 0 
        right = n - 1
        while left <= right:
            mid = int((left+right)/2)
            if matrix[ind][mid] == target:
                return True
            elif matrix[ind][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False