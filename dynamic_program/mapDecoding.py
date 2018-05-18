def mapDecoding(message):
    if not message:
        return 1
    
    if len(message) == 1:
        return int(int(message) != 0)
    
    if len(message) == 2:
        count = int(9 < int(message) < 27)
        count += int(int(message[0]) != 0 and int(message[1]) != 0)
        return count
    
    first = int(int(message[0]) != 0)
    second = int(9 < int(message[0:2]) < 27)
    second += int(int(message[0]) != 0 and int(message[1]) != 0)
    m = (10**9 + 7)
    for i in range(2, len(message)):
        third = 0
        if int(message[i]) != 0:
            third += second
        if 9 < int(message[i-1:i+1]) < 27:
            third += first
        first = second % m
        second = third % m
        
    return second % m

