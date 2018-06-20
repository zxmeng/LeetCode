def findMaxForm(self, strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    
    if not strs:
        return 0
    
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    
    for s in strs:
        zeros, ones = s.count("0"), s.count("1")
        for i in range(m, zeros-1, -1):
            for j in range(n, ones-1, -1):
                dp[i][j] = max(dp[i-zeros][j-ones]+1, dp[i][j])
                
    return dp[-1][-1]