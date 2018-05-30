def helper(self, string, n, pushed, poped, res):
    if poped > pushed:
        return 
    
    # if pushed == n and poped == n:
    #     res.append(string)
    #     return
    
    if pushed == n:
        string += ")" * (n-poped)
        res.append(string)
        return
     
    if pushed < n:
        self.helper(string + "(", n, pushed+1, poped, res)
    if poped < n:
        self.helper(string + ")", n, pushed, poped+1, res)
        
def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    
    if n == 0:
        return []
    if n == 1:
        return ["()"]
    
    res = []
    self.helper("(", n, 1, 0, res)
    
    return res