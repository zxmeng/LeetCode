def firstDuplicate(a):
    
    for i in range(len(a)):
        index = abs(a[i]) - 1
        if a[index] < 0:
            return abs(a[i])
        else:
            a[index] *= -1
    return -1