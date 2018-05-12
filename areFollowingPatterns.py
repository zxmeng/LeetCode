def areFollowingPatterns(strings, patterns):
	dic = {}
	for i in range(len(strings)):
		if patterns[i] not in dic:
			dic[patterns[i]] = strings[i]
		elif dic[patterns[i]] != strings[i]:
			return False
		
	dic = {}
	for i in range(len(strings)):
		if strings[i] not in dic:
			dic[strings[i]] = patterns[i]
		elif dic[strings[i]] != patterns[i]:
			return False

	return True


