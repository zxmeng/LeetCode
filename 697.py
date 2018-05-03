class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        frequency = [ 0 for x in range(max(nums) + 1)]
        first = [ 0 for x in range(max(nums) + 1)]
        last = [ 0 for x in range(max(nums) + 1)]
        
        for i in range(len(nums)):
            if (frequency[nums[i]] == 0):
                frequency[nums[i]] = 1
                first[nums[i]] = i
                last[nums[i]] = i
            else:
                frequency[nums[i]] += 1
                last[nums[i]] = i
                
        temp = 0
        re = 1
        for i in range(len(nums)):
            if (frequency[nums[i]] > temp):
                temp = frequency[nums[i]]
                re = 1 + last[nums[i]] - first[nums[i]]
            elif (frequency[nums[i]] == temp):
                if (1 + last[nums[i]] - first[nums[i]] < re):
                    re = 1 + last[nums[i]] - first[nums[i]]
                
        return re


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        frequency = {}
        first = {}
        last = {}
        
        for i in range(len(nums)):
            if (nums[i] not in frequency):
                frequency[nums[i]] = 1
                first[nums[i]] = i
                last[nums[i]] = i
            else:
                frequency[nums[i]] += 1
                last[nums[i]] = i
                
        temp = 0
        re = 1
        for num in set(nums):
            if (frequency[num] > temp):
                temp = frequency[num]
                re = 1 + last[num] - first[num]
            elif (frequency[num] == temp):
                if (1 + last[num] - first[num] < re):
                    re = 1 + last[num] - first[num]
                
        return re