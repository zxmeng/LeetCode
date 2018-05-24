def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        
        dp = [[0 for i in range(K)] for j in range(len(A))]
        count = 0.0
        for i in range(len(A)):
            count += A[i]
            dp[i][0] = count/(i+1.0)
        
        for k in range(1, K):
            for i in range(k,len(A)):
                for j in range(k-1, i):
                    dp[i][k] = max(dp[i][k], dp[j][k-1] + sum(A[j+1:i+1])/(i-j))
        
        return dp[-1][-1]


def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        
        dp = [0 for j in range(len(A))]
        count = 0.0
        for i in range(len(A)):
            count += A[i]
            dp[i] = count/(i+1.0)
        
        for k in range(1, K):
            dp_temp = [0 for j in range(len(A))]
            for i in range(k,len(A)):
                for j in range(k-1, i):
                    dp_temp[i] = max(dp_temp[i], dp[j] + sum(A[j+1:i+1])/(i-j))
            dp = dp_temp
        return dp[-1]