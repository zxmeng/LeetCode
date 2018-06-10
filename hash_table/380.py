class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.nums = []
        self.ind = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.ind:
            self.nums.append(val)
            self.ind[val] = len(self.nums) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val in self.ind:
            last = self.nums[-1]
            ind = self.ind[val]
            self.nums[ind] = last
            self.ind[last] = ind
            self.nums.pop()
            del self.ind[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        r = random.randint(0, len(self.nums) - 1)
        return self.nums[r]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()