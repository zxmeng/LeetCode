def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        min_jumps = [ len(nums) for i in range(len(nums)) ]
        
        min_jumps[0] = 0
        
        reach = 0
        i = 0
        while i < min(reach+1, len(nums)):
            if reach < nums[i] + i:
                for j in range(reach, min(nums[i]+i+1, len(nums))):
                    min_jumps[j] = min(min_jumps[j], min_jumps[i]+1)
            reach = max(reach, nums[i]+i)
            i += 1
                
        return min_jumps[-1]


def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        min_jumps = [ len(nums) for i in range(len(nums)) ]
        
        min_jumps[0] = 0
        
        reach = 0
        i = 0
        # step = 0
        while i < min(reach+1, len(nums)):
            if reach < nums[i] + i:
                for j in range(reach+1, min(nums[i]+i+1, len(nums))):
                    min_jumps[j] = min_jumps[i]+1
            reach = max(reach, nums[i]+i)
            i += 1
                
        return min_jumps[-1]