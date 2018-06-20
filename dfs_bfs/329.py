class Solution:
    row = 0
    col = 0
    dp = []
    
    def dfs(self, matrix, i, j):
        max_len = 1
        for [dx, dy] in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            r = i + dx
            c = j + dy
            if 0 <= r < self.row and 0 <= c < self.col and matrix[r][c] > matrix[i][j]:
                if not self.dp[r][c]:
                    self.dp[r][c] = self.dfs(matrix, r, c)
                max_len = max(max_len, 1 + self.dp[r][c])
        
        return max_len
        
        
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        if not matrix or not matrix[0]:
            return 0
        
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.dp = [[0 for _ in range(self.col)] for _ in range(self.row)]
        
        max_len = 0
        for i in range(self.row):
            for j in range(self.col):
                self.dp[i][j] = self.dfs(matrix, i, j)
                max_len = max(max_len, self.dp[i][j])
                
        return max_len
        