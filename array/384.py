class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.ori = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        
        self.nums = self.ori[:]
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        
        for i in range(len(self.nums)):
            ind = random.randint(i, len(self.ori)-1)
            temp = self.nums[i]
            self.nums[i] = self.nums[ind]
            self.nums[ind] = temp
            
        return self.nums