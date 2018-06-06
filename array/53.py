def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        re = [0 for i in range(len(nums))]
        re[0] = nums[0]
        for i in range(1, len(nums)):
            re[i] = max(nums[i], nums[i] + re[i-1])
            
        return max(re)

def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        re = nums[0]
        cur_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], nums[i] + cur_max)
            re = max(re, cur_max)
            
        return re