def possibleSums(coins, quantity):
	re = []
	
	for i in range(len(coins)):
		if len(re) == 0:
			re = [j*coins[i] for j in range(1, quantity[i]+1)]
		else:
			re += [j*coins[i]+num for j in range(1, quantity[i]+1) for num in re + [0]]
			
	return len(set(re))