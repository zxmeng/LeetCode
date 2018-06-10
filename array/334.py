def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if not nums:
            return False
        
        left_min = max(nums)
        sec_min = max(nums)
        
        for el in nums:
            if el > sec_min:
                return True
            
            if el <= left_min:
                left_min = el
            elif el < sec_min:
                sec_min = el
                
        return False