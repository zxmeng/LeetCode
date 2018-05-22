def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) < 2:
            return 0
        
        buy = [0 for i in range(len(prices))]
        sell = [0 for i in range(len(prices))]
        
        buy[0] = - prices[0]
        sell[0] = 0
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(prices[1] - prices[0], sell[0])
        
        for i in range(2, len(prices)):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            
        return sell[-1]