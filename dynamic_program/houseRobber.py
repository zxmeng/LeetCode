def houseRobber(nums):
    if not nums:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    if len(nums) == 2:
        return max(nums)
    
    re = [0] * len(nums)
    re[0] = nums[0]
    re[1] = max(nums[0], nums[1])
    
    for i in range(2, len(re)):
        re[i] = max(re[i-1], re[i-2] + nums[i])
        
    return re[-1]