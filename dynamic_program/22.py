import copy

class Solution:
    def next_is_push(self, stack, n, pushed, poped):
        if pushed == n-1:
            for i in range(len(stack)):
                stack[i] += "(" + ")" * (n-poped)
            return stack
        
        for i in range(len(stack)):
            stack[i] += "("
        pushed += 1
        return self.next_is_pop(copy.deepcopy(stack), n, pushed, poped) + self.next_is_push(copy.deepcopy(stack), n, pushed, poped) 
        
    def next_is_pop(self, stack, n, pushed, poped):
        if poped >= pushed:
            return []
        
        for i in range(len(stack)):
            stack[i] += ")"
        poped += 1
        return self.next_is_pop(copy.deepcopy(stack), n, pushed, poped) + self.next_is_push(copy.deepcopy(stack), n, pushed, poped) 
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        
        stack = ["("]
        pushed = 1
        poped = 0
        
        return self.next_is_pop(copy.deepcopy(stack), n, pushed, poped) + self.next_is_push(copy.deepcopy(stack), n, pushed, poped) 