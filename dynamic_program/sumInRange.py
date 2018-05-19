def sumInRange(nums, queries):
    partialSum = [ 0 for i in range(len(nums)) ]
    partialSum[0] = nums[0]
    for i in range(1, len(nums)):
        partialSum[i] = partialSum[i-1] + nums[i]
        
    count = 0
    for q in queries:
        count += partialSum[q[1]] - partialSum[q[0]] + nums[q[0]]
        count %= (10 ** 9 + 7)
        
    return count % (10 ** 9 + 7)