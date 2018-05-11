def isListPalindrome(l):
    if not l:
        return True
    if not l.next:
        return True
    if not l.next.next:
        return l.value == l.next.value
    
    head = l
    
    fast = head
    slow = head
    prev = head
    while fast and fast.next and slow:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    prev.next = None

    # even len
    if not fast:
        pass
    # odd len
    else:
        slow = slow.next
        
    tail = slow
    node = slow.next
    left = slow
    left.next = None
    while node:
        right = node.next
        node.next = left
        left = node
        tail = node
        node = right
        
    while head and tail:
        if head.value != tail.value:
            return False
        
        head = head.next
        tail = tail.next
        
    return True