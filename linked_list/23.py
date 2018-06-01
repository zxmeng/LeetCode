# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if not lists:
            return None
        
        for i in range(len(lists)-1, -1, -1):
            if not lists[i]:
                del lists[i]
        
        if not lists:
            return None
        
        k = len(lists)
        min_val = lists[0].val
        ind = 0
        
        for i in range(1, k):
            if lists[i].val < min_val:
                min_val = lists[i].val
                ind = i
                
        root = lists[ind]
        lists[ind] = lists[ind].next
        if not lists[ind]:
            del lists[ind]
        node = root

        while lists:
            k = len(lists)
            min_val = lists[0].val
            ind = 0

            for i in range(1, k):
                if lists[i].val < min_val:
                    min_val = lists[i].val
                    ind = i
            
            node.next = lists[ind]
            lists[ind] = lists[ind].next
            node = node.next
            
            if not lists[ind]:
                del lists[ind]
                
        return root