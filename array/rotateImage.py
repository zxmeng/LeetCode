def rotateImage(a):
    n = len(a) - 1
    
    for i in range(n+1):
        for j in range(i, n-i):
            temp = a[i][j]
            a[i][j] = a[n-j][i]
            a[n-j][i] = a[n-i][n-j]
            a[n-i][n-j] = a[j][n-i]
            a[j][n-i] = temp
            
    return a