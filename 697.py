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


# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6