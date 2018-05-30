def helper(self, nums, perm, res):
        if not nums:
            res.append(perm)
        else:
            for i in range(len(nums)):
                self.helper(nums[:i] + nums[i+1:], perm + [nums[i]], res)
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        self.helper(nums, [], res)
        return res