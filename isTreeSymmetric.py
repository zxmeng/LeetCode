def isTreeSymmetric(t):
	if not t:
		return True

	nodes = [t.left, t.right]
	while len(nodes) > 0:
		temp = []
		for i in range(len(nodes)):
			if nodes[i]:
				if not nodes[-(i+1)]:
					return False
				elif nodes[i].value != nodes[-(i+1)].value:
					return False
				temp += [nodes[i].left, nodes[i].right]
			else:
				if nodes[-(i+1)]:
					return False
		nodes = temp
	return True