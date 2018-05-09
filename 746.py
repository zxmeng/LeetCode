def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        counter = [ 0 for i in range(len(cost)) ]
        
        for i in range(2, len(cost)):
            counter[i] = min(counter[i-2] + cost[i-2], counter[i-1] + cost[i-1])
            
        return min(counter[-1] + cost[-1], counter[-2] + cost[-2])