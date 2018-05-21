def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        max_profit = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > cur_min:
                max_profit = max(max_profit, prices[i] - cur_min)
            else:
                cur_min = prices[i]
                
        return max_profit