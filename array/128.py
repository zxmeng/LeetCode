def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    if not nums:
        return 0
    
    min_heap = []
    
    for el in set(nums):
        heapq.heappush(min_heap, el)
        
    prev = heapq.heappop(min_heap)
    max_count = 0
    count = 1
    while min_heap:
        num = heapq.heappop(min_heap)
        if num == prev + 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 1
        prev = num
    return max(count, max_count)


def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    if not nums:
        return 0
    
    count = 0
    max_count = 0
    nums_set = set(nums)
    
    for el in nums_set:
        if el - 1 not in nums_set:
            temp = el + 1
            count = 1
            while temp in nums_set:
                temp += 1
                count += 1
            max_count = max(count, max_count)
            
    return max(count, max_count)