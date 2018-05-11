def reverse(list):
    if not list or not list.next:
        return list, list
    if not list.next.next:
        head = list.next
        head.next = list
        list.next = None
        return head, list
    
    node = list.next
    list.next = None
    left = list
    tail = None
    while node:
        right = node.next
        node.next = left
        left = node
        tail = node
        node = right
    return tail, list


def reverseNodesInKGroups(l, k):
    if k <= 1:
        return l
    
    count = 0
    head = l
    node = l
    tail = l
    while count < k and node:
        tail = node
        node = node.next
        count += 1
        
    if count < k:
        return l
    else:    
        newHead = tail.next
        tail.next = None
        finalHead, newTail = reverse(head)
        
    while newHead:
        count = 0
        head = newHead
        node = newHead
        tail = newHead
        while count < k and node:
            tail = node
            node = node.next
            count += 1
        
        if count < k:
            newTail.next = head
            break
        else:
            newHead = tail.next
            tail.next = None
            head, tail = reverse(head)
            newTail.next = head
            newTail = tail
    
    return finalHead

    