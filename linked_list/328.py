def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    if not head or not head.next:
        return head
    
    odd_tail = head
    even_head = head.next
    even_tail = head.next
    node = head.next.next
    
    odd_tail.next = None
    even_tail.next = None
    i = 3
    while node:
        if i % 2 == 1:
            odd_tail.next = node
            node = node.next
            odd_tail = odd_tail.next
            odd_tail.next = None
        else:
            even_tail.next = node
            node = node.next
            even_tail = even_tail.next
            even_tail.next = None
        i += 1
        
    odd_tail.next = even_head
    return head