def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) < 3:
            return False
        
        
        unused = {}
        need = {}
        
        for el in nums:
            if el not in unused:
                unused[el] = 0
            unused[el] += 1
            
        for i in range(len(nums)):
            if unused[nums[i]] == 0:
                continue
            elif nums[i] in need and need[nums[i]] > 0:
                unused[nums[i]] -= 1
                need[nums[i]] -= 1
                if nums[i] + 1 not in need:
                    need[nums[i]+1] = 0
                need[nums[i]+1] += 1
            elif nums[i]+1 in unused and unused[nums[i]+1] > 0 and nums[i]+2 in unused and unused[nums[i]+2] > 0:
                unused[nums[i]] -= 1
                unused[nums[i]+1] -= 1
                unused[nums[i]+2] -= 1
                if nums[i] + 3 not in need:
                    need[nums[i]+3] = 0
                need[nums[i]+3] += 1
            else:
                return False
            
        return True