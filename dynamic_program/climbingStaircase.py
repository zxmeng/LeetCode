def climbingStaircase(n, k):
    if n == 0:
        return [[]]
    if k == 0:
        return [[]]
    
    re = {0:[[]], 1:[[1]]}
    for i in range(2, n+1):
        re[i] = []
        for j in range(1, min(k, i)+1):
            re[i] += [el + [j] for el in re[i-j]]
            
    return sorted(re[n])