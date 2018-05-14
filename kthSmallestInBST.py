#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

import heapq

def kthSmallestInBST(t, k):
	nodes = [t]
	maxHeap = []
	
	while nodes:
		temp = []
		for node in nodes:
			heapq.heappush(maxHeap, - node.value)
			
			if len(maxHeap) > k:
				heapq.heappop(maxHeap)
				
			if node.left:
				temp.append(node.left)
			if node.right:
				temp.append(node.right)
				
		nodes = temp
		
	return - maxHeap[0]