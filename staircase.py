counter = [0, 1, 2, 4]
s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    if n >= len(counter):
        for i in range(len(counter), n+1):
            temp = counter[i-1]+counter[i-2]+counter[i-3]
            counter.append(temp)
    print counter[n]