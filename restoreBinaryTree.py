#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#

def restoreBinaryTree(inorder, preorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return Tree(inorder[0])

    root = None

    for i in range(len(inorder)):
        if inorder[i] == preorder[0]:
            root = Tree(inorder[i])
            root.left = restoreBinaryTree(inorder[:i], preorder[1:i+1])
            root.right = restoreBinaryTree(inorder[i+1:], preorder[i+1:])
            break
        
    return root