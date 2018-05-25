def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if not nums:
            return False
        
        reach = 0
        i = 0
        while i < min(reach+1, len(nums)):
            reach = max(i+nums[i], reach)
            i += 1
            
        return reach >= len(nums) - 1