# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, head):
        if not head.next:
            return head, head
        
        newhead, tail = self.reverse(head.next)
        tail.next = head
        head.next = None
        
        return newhead, head
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        if not head.next:
            return head
        
        newhead, tail = self.reverse(head.next)
        tail.next = head
        head.next = None
        
        return newhead


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        if not head.next.next:
            newhead = head.next
            newhead.next = head
            head.next = None
            return newhead
        
        left = head
        cur = head.next
        left.next = None
        while cur.next:
            right = cur.next
            cur.next = left
            left = cur
            cur = right
        cur.next = left
        return cur