def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(nums) < 4:
            return []
        
        two_sum = {}
        nums.sort()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp = nums[i]+nums[j]
                if nums[i]+nums[j] not in two_sum:
                    two_sum[temp] = []
                two_sum[temp].append([i, j])
                
        re = set()
        for i in range(2, len(nums)):
            for j in range(i+1, len(nums)):
                temp = target - nums[i] -nums[j]
                if temp in two_sum:
                    for el in two_sum[temp]:
                        if i > el[1]:
                            re.add((nums[el[0]], nums[el[1]], nums[i], nums[j]))
                                       
        return [list(el) for el in re]