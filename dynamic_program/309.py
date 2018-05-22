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


def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) < 2:
            return 0
        
        buy = 0
        pre_sell = 0
        pre_buy = max(-prices[0], -prices[1])
        sell = max(prices[1] - prices[0], pre_sell)
        
        for i in range(2, len(prices)):
            buy = max(pre_buy, pre_sell - prices[i])
            pre_sell = sell
            sell = max(pre_sell, pre_buy + prices[i])
            pre_buy = buy
            
        return sell