""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST_iter(root):
    if root.left == None:
        if root.right == None:
            return True, root.data, root.data
        else:
            flag, min, max = checkBST_iter(root.right)
            return flag and root.data < min, root.data, max
    else:
        if root.right == None:
            flag, min, max = checkBST_iter(root.left)
            return flag and root.data > max, min, root.data
        else:
            flag_l, min_l, max_l = checkBST_iter(root.left)
            flag_r, min_r, max_r = checkBST_iter(root.right)
            return flag_l and flag_r and max_l < root.data < min_r, min_l, max_r

def checkBST(root):
    if root.left == None:
        if root.right == None:
            return True
        else:
            flag, min, max = checkBST_iter(root.right)
            return flag and root.data < min
    else:
        if root.right == None:
            flag, min, max = checkBST_iter(root.left)
            return flag and root.data > max
        else:
            flag_l, min_l, max_l = checkBST_iter(root.left)
            flag_r, min_r, max_r = checkBST_iter(root.right)
            return flag_l and flag_r and max_l < root.data < min_r

