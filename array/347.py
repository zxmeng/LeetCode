def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        fre = {}
        for el in nums:
            if el not in fre:
                fre[el] = 0
            fre[el] += 1
            
        max_heap = []
        for el in fre:
            heapq.heappush(max_heap, (-fre[el], el))
            
        re = []
        for i in range(k):
            re.append(heapq.heappop(max_heap)[1])

                
        return re


# bucket sort
def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        fre = {}
        max_fre = 0
        for el in nums:
            if el not in fre:
                fre[el] = 0
            fre[el] += 1
            max_fre = max(max_fre, fre[el])
            
        bucket = [[] for i in range(max_fre)]
        for el in fre:
            bucket[fre[el]-1].append(el)
        
        re = []
        for i in range(max_fre):
            re += bucket[-i-1]
            if len(re) >= k:
                break
                
        return re[:k]