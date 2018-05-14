def merge(pairs):
	set_list = []
	for pair in pairs:
		swap_set = set([el - 1 for el in pair])

		found = -1
		remove = -1
		for i in range(len(set_list)):
			if set_list[i] & swap_set:
				if found == -1:
					set_list[i] = set_list[i] | swap_set
					found = i
				else:
					set_list[found] |= set_list[i] 
					remove = i

		if found == -1:
			set_list.append(swap_set)

		if remove != -1:
			del set_list[remove]

	return set_list

def swapLexOrder(str, pairs):
	if len(pairs) == 0:
		return str
	
	cluster = merge(pairs)

	temp_list = list(str)
	for cl in cluster:
		c = sorted(list(cl))
		
		temp_swap = []
		for el in c:
			temp_swap.append(temp_list[el])
		temp_swap.sort()
		
		for i in range(len(c)):
			temp_list[c[i]] = temp_swap[-(i+1)]

	return "".join(temp_list)

		