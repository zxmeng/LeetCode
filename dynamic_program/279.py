class Solution:
    _dp = [0, 1]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = self._dp
        while len(dp) <= n:
            sqrt = math.sqrt(len(dp))
            floor = int(math.floor(sqrt))
            dp += [1 + min([dp[len(dp) - j ** 2] for j in range(1, floor+1)])]
            
        return dp[n]