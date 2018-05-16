# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    while(l != None and l.value == k):
        l = l.next
    
    if l != None:
        node = l
        while(node.next != None):
            if node.next.value != k:
                node = node.next
            else:
                node.next = node.next.next
            
    return l