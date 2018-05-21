def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height) < 3:
            return 0
        
        left_max = [0 for i in range(len(height))]
        right_max = [0 for i in range(len(height))]
        
        cur_max = height[0]
        for i in range(1, len(height)):
            left_max[i] = cur_max
            cur_max = max(cur_max, height[i])
            
        cur_max = height[-1]
        for i in range(1, len(height)):
            right_max[-i-1] = cur_max
            cur_max = max(cur_max, height[-i-1])
            
        total = 0
        for i in range(1, len(height)-1):
            min_h = min(left_max[i], right_max[i])
            if height[i] < min_h:
                total += min_h - height[i]
        
        return total