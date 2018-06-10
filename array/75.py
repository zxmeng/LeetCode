def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if not nums or len(nums) == 1:
            return
        
        start_one = -1
        start_two = -1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                if start_one == -1 and start_two == -1:
                    continue
                elif start_two == -1:
                    nums[i] = 1
                    nums[start_one] = 0
                    start_one += 1
                elif start_one == -1:
                    nums[i] = 2
                    nums[start_two] = 0
                    start_two += 1
                else:
                    nums[i] = 2
                    nums[start_two] = 1
                    nums[start_one] = 0
                    start_one += 1
                    start_two += 1
            elif nums[i] == 1:
                if start_one == -1 and start_two == -1:
                    start_one = i
                elif start_two == -1:
                    continue
                elif start_one == -1:
                    nums[i] = 2
                    nums[start_two] = 1
                    start_one = start_two
                    start_two += 1
                else:
                    nums[i] = 2
                    nums[start_two] = 1
                    start_two += 1
            else:
                if start_two == -1:
                    start_two = i
                    
        return