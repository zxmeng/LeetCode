class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        
        row = len(M)
        col = len(M[0])
        
        ans = [ [0] * col for x in range(row) ]
        
        for i in range(row):
            for j in range(col):
                temp = 0
                count = 0
                for k in (i, i+1, i-1):
                    for t in (j, j+1, j-1):
                        if (k>= 0 and k <row and t>=0 and t<col):
                            temp += M[k][t]
                            count += 1
                
                ans[i][j] = temp/count
            
        return ans