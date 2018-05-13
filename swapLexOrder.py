def merge(pairs):
	re = {}

	for pair in pairs:
		a = min(pair) - 1
		b = max(pair) - 1

		if a not in re:
			re[a] = set([a])
		if b not in re:
			re[b] = set([b])
		
		re[b] = re[b].union(re[a])
		re[a] = re[a].union(re[b])
		
	return re

def swapLexOrder(str, pairs):
	if len(pairs) == 0:
		return str
	
	cluster = merge(pairs)

	temp_list = list(str)
	for cl in cluster:
		c = sorted(list(cluster[cl]))
		
		temp_swap = []
		for el in c:
			temp_swap.append(temp_list[el])
		temp_swap.sort()
		for i in range(len(c)):
			temp_list[c[i]] = temp_swap[-(i+1)]
			
	out = ""
	for el in temp_list:
		out += el

	return out

		