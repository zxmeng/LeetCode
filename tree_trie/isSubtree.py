#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#     

def check(t1, t2):
	if not t1 and not t2:
		return True
	if not t1 or not t2:
		return False
	if t1.value != t2.value:
		return False
	
	return check(t1.left, t2.left) and check(t1.right, t2.right)
	
def isSubtree(t1, t2):
	if not t2:
		return True
	if not t1:
		return False
	
	return check(t1, t2) or isSubtree(t1.left, t2) or isSubtree(t1.right, t2)
