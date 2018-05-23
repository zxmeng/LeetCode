def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        re = ["" for i in range(n)]
        
        for i in range(n):
            if (i+1) % 3 == 0:
                re[i] += "Fizz"
            if (i+1) % 5 == 0:
                re[i] += "Buzz"
            if re[i] == "" :
                re[i] = str(i+1)
                
        return re