class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        
def add(node, contact):
    for char in contact:
        if char not in node.children:
            node.children[char] = Node()
        node.children[char].count += 1
        node = node.children[char]

def find(node, contact):
    for char in contact:
        if char not in node.children:
            return 0
        node = node.children[char]
    return node.count

n = int(raw_input().strip())
contacts = Node()
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    
    if op == "add":
        add(contacts, contact)
    elif op == "find":
        print find(contacts, contact)