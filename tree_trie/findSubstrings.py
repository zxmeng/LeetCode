class Node():
	def __init__(self, x):
		self.value = x
		self.child = {}
		self.end = False

def buildTrie(parts):
	root = Node(" ")
	for part in parts:
		node = root
		for el in part:
			if el not in node.child:
				node.child[el] = Node(el)
			node = node.child[el]
		node.end = True
	return root

def findSubstrings(words, parts):
	if not words or not parts:
		return words
	
	root = buildTrie(parts)
	
	for k in range(len(words)):
		word = words[k]
		max_len = 0
		max_str = ""
		min_ind = len(word)
		flag = False
		
		for i in range(len(word)):
			if word[i:i+1] in root.child:
				node = root
				for j in range(i, len(word)):
					if word[j:j+1] in node.child:
						node = node.child[word[j:j+1]]
						if node.end and j - i + 1 > max_len:
							max_len = j - i + 1
							max_str = word[i:j+1]
							min_ind = i
							flag = True
					else:
						break

		if flag:
			words[k] = word[:min_ind] + "[" + max_str + "]" + word[min_ind+max_len:]
		
	return words
				
				