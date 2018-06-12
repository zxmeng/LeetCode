def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        dp_len = [1 for i in range(len(nums))]
        dp_count = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp_len[j] + 1 > dp_len[i]:
                        dp_len[i] = dp_len[j] + 1
                        dp_count[i] = dp_count[j]
                    elif dp_len[j] + 1 == dp_len[i]:
                        dp_count[i] += dp_count[j]
            
        max_len = max(dp_len)
        max_count = 0
        for i in range(len(nums)):
            if dp_len[i] == max_len:
                max_count += dp_count[i]
            
        return max_count