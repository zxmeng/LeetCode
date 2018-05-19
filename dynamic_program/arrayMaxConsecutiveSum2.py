def arrayMaxConsecutiveSum2(inputArray):
    part_max = 0
    total_max = inputArray[0]
    
    for el in inputArray:
        part_max += el
        
        if part_max < el:
            part_max = el
        if part_max > total_max:
            total_max = part_max
            
    return total_max