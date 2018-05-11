def reverse(list):
    if not list or not list.next:
        return list
    if not list.next.next:
        head = list.next
        head.next = list
        list.next = None
        return head
    
    left = list
    node = list.next
    left.next = None
    tail = None
    while node:
        right = node.next
        node.next = left
        left = node
        tail = node
        node = right
    return tail
        
def addTwoHugeNumbers(a, b):

    a = reverse(a)
    b = reverse(b)
    head = ListNode(0)
    node = head
    prev = head
    re = 0
    while a and b:
        sum = str(a.value + b.value + re)
        if len(sum) > 4:
            re = int(sum[:-4])
            node.value = int(sum[-4:])
        else:
            node.value = int(sum)
            re = 0
        node.next = ListNode(0)
        prev = node
        node = node.next
        a = a.next
        b = b.next
        
    if a:
        while a:
            sum = str(a.value + re)
            if len(sum) > 4:
                re = int(sum[:-4])
                node.value = int(sum[-4:])
            else:
                node.value = int(sum)
                re = 0
            node.next = ListNode(0)
            prev = node
            node = node.next
            a = a.next
        
    elif b:
        while b:
            sum = str(b.value + re)
            if len(sum) > 4:
                re = int(sum[:-4])
                node.value = int(sum[-4:])
            else:
                node.value = int(sum)
                re = 0
            node.next = ListNode(0)
            prev = node
            node = node.next
            b = b.next
    
    if re == 0:
        prev.next = None
    else:
        node.value = re
        
    return reverse(head)
    