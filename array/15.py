def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) < 3:
            return []
        
        nums.sort()
        re = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                target = -nums[i]
                left = i+1
                right = len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == target:
                        re.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    else:
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
            
                    
        return re