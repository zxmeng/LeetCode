def mergeTwoLinkedLists(l1, l2):
    if not l1 and not l2:
        return None
    
    head = ListNode(0)
    node = head
    prev = head
    
    while l1 and l2:
        if l1.value <= l2.value:
            node.value = l1.value
            l1 = l1.next
        else:
            node.value = l2.value
            l2 = l2.next
            
        node.next = ListNode(0)
        prev = node
        node = node.next
        
    while l1:
        node.value = l1.value
        l1 = l1.next
        node.next = ListNode(0)
        prev = node
        node = node.next
            
    while l2:
        node.value = l2.value
        l2 = l2.next
        node.next = ListNode(0)
        prev = node
        node = node.next
        
    prev.next = None
    
    return head