import math

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    flag = False
    if n < 2:
        flag = True
    elif n == 2:
        flag = False
    else:
        for i in range(2, int(math.ceil(math.sqrt(n)))+1):
            if n%i == 0:
                flag = True
                break
    if flag:
        print "Not prime"
    else:
        print "Prime"