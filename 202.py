def helper(self, n, visited):
        if n in visited:
            return False
        
        visited.append(n)
        re = 0
        for el in list(str(n)):
            re += int(el) ** 2
            
        if re == 1:
            return True
            
        return self.helper(re, visited)
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        visited = [n]
        re = 0
        for el in list(str(n)):
            re += int(el) ** 2
            
        if re == 1:
            return True
            
        return self.helper(re, visited)