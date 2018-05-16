#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#     

def dfs(node, prefix):
	if not node:
		return 0
	
	if not node.left and not node.right:
		return int(prefix + str(node.value))
	
	prefix += str(node.value)
	return dfs(node.left, prefix) + dfs(node.right, prefix)
	
def digitTreeSum(t):
	return dfs(t, "")
	

