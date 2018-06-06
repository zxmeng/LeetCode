def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums)
        
        re = [0 for i in range(len(nums)-1)]
        # choose 0, then not n-1
        re[0] = nums[0]
        re[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            re[i] = max(nums[i]+re[i-2], re[i-1])
        
        cur_max = re[-1]
        # not choose 0, then n-1
        re = [0 for i in range(len(nums)-1)]
        re[0] = nums[1]
        re[1] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            re[i-1] = max(nums[i]+re[i-3], re[i-2])
            
        return max(cur_max, re[-1])