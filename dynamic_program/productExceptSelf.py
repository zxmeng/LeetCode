def productExceptSelf(nums, m):
    prefix = [1 for i in range(len(nums))]
    for i in range(1, len(nums)):
        prefix[i] = ( prefix[i-1] * nums[i-1] ) % m
        
    suffix = 1
    g = 0
    for i in range(len(nums)):
        g += (prefix[-1-i] * suffix) % m
        suffix = (suffix * nums[-1-i]) % m
        
    return g % m
    