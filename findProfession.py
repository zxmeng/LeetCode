import math

def helper(pos):
    if pos == 0:
        return 1
    if pos == 1:
        return 0
    
    else: 
        level = math.floor(math.log(pos, 2))
        if level % 2 == 0:
            return 1 - helper(pos-2**level)
        else:
            return helper(2**(level+1)-pos-1)
            
def findProfession(level, pos):
	l = helper(pos-1)
	if l == 1:
		return "Engineer"
	else:
		return "Doctor"
 