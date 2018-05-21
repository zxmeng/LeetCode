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

def trap_2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height) < 3:
            return 0
        
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        total = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]
                right -= 1
                
        return total

def trap_3(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height) < 3:
            return 0
        
        left = 1
        right = len(height) - 2
        left_max = height[0]
        right_max = height[-1]
        total = 0
        while left <= right:
            if left_max < right_max:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]
                right -= 1
                
        return total