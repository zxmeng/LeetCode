class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        for i in range(len(prices) - 1):
            temp = prices[i+1] - prices[i]
            if (temp > 0):
                max_profit += temp
            
        return max_profits