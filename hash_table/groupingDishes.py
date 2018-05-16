def groupingDishes(dishes):
	dic = {}

	for dish in dishes:
		for ing in dish[1:]:
			if ing not in dic:
				dic[ing] = []  
			dic[ing].append(dish[0])

	output = []
	for ing in sorted(dic):
		if len(dic[ing]) >= 2:
			output.append([ing] + sorted(dic[ing]))

	return output