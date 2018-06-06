def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        nums.sort()
        for i in range(len(nums)-1, -1, -1):
            l = 0
            r = i-1
            while l < r:
                if nums[l] + nums[r] <= nums[i]:
                    l += 1
                else:
                    count += r - l
                    r -= 1
                    
        return count