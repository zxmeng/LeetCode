def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = max(nums)
        n = len(nums)
        
        pos_max = [0 for i in range(n)]
        neg_min = [0 for i in range(n)]
        
        if nums[0] > 0:
            pos_max[0] = nums[0]
        else:
            neg_min[0] = nums[0]
        
        for i in range(1, n):
            pos_max[i] = max(0, pos_max[i-1] * nums[i], nums[i], neg_min[i-1] * nums[i])
            neg_min[i] = min(0, pos_max[i-1] * nums[i], nums[i], neg_min[i-1] * nums[i])
            m = max(m, pos_max[i])
            
        return m