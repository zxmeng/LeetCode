def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        re = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    re[i] = max(re[i], re[j]+1)
                    
        return max(re)

def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        re = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] > re[-1]:
                re.append(nums[i])
            else:
                left = 0 
                right = len(re) - 1
                while left <= right:
                    mid = int((left + right)/2)
                    if re[mid] >= nums[i]:
                        right = mid - 1
                    else:
                        left = mid + 1
                re[left] = nums[i]
                
        return len(re)