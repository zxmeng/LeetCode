def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        first = [0 for i in range(len(prices))]
        second = [0 for i in range(len(prices))]
        
        max_pro = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
            max_pro = max(max_pro, prices[i] - cur_min)
            first[i] = max_pro
            
        max_pro = 0
        cur_max = prices[-1]
        for i in range(1, len(prices)):
            if prices[-1-i] > cur_max:
                cur_max = prices[-1-i]
            max_pro = max(max_pro, cur_max - prices[-1-i])
            second[-1-i] = max_pro
                
        max_pro = 0
        for i in range(len(prices)):
            max_pro = max(max_pro, first[i] + second[i])
                 
        return max_pro