#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#    

def findMostRight(t):
	while t.right:
		t = t.right
	return t.value

def removeMostRight(t):
    if t.right:
        t.right = removeMostRight(t.right)
    else:
        t = t.left
    return t

def delete(t, q):
	if not t:
		return t

	if q == t.value:
		if t.left:
			t.value = findMostRight(t.left)
			t.left = removeMostRight(t.left)
		else:
			t = t.right
	elif q < t.value:
		t.left = delete(t.left, q)
	else:
		t.right = delete(t.right, q)

	return t
		
def deleteFromBST(t, queries):
	if not t:
		return t

	for q in queries:
		t = delete(t, q)

	return t
				
				