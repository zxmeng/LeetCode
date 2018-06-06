def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 1
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i += 1
            else:
                nums[count] = nums[i]
                count += 1
                i += 1
                
        del nums[count:]
        return len(nums)