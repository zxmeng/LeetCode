#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def dfs(t, s):
	if not t:
		return False
	
	s -= t.value
	if not t.left and not t.right:
		return s == 0
	
	return dfs(t.left, s) or dfs(t.right, s)

def hasPathWithGivenSum(t, s):
	if not t:
		return s == 0
	
	s -= t.value
	if not t.left and not t.right:
		return s == 0
	
	return dfs(t.left, s) or dfs(t.right, s)




