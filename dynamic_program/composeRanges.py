def composeRanges(nums):
    if not nums:
        return nums
    
    start = nums[0]
    end = nums[0]
    re = []
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            end = nums[i]
            i += 1
        else:
            if start == end:
                re += [str(start)]
            else:
                re += [str(start) + "->" + str(end)]
            start = nums[i]
            end = nums[i]
            
    if start == end:
        re += [str(start)]
    else:
        re += [str(start) + "->" + str(end)]
        
    return re
                

