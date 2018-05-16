def rearrangeLastN(l, n):
    if not l:
        return l
    if n == 0:
        return l
    
    count = 0
    node = l
    while node:
        node = node.next
        count += 1
        
    if n >= count:
        return l
    
    node = l
    prev = l
    while count > n:
        prev = node
        node = node.next
        count -= 1
        
    prev.next = None
    head = node
    while node.next:
        node = node.next
        
    node.next = l
    return head