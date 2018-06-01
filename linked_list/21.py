# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        root = None
        if l1.val < l2.val:
            root = l1
            l1 = l1.next
        else:
            root = l2
            l2 = l2.next
            
        node = root
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
            
        if l1:
            node.next = l1
        elif l2:
            node.next = l2
        else:
            node.next = None
            
        return root