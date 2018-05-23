def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return []
        
        right = [1 for i in range(len(nums))]
        
        re_r = 1
        for i in range(1, len(nums)):
            re_r *= nums[-i]
            right[-i-1] = re_r
            
        left = 1
        for i in range(len(nums)):
            right[i] = left * right[i]
            left *= nums[i]
            
        return right