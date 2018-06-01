def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        row = len(matrix)
        
        max_heap = []
        for i in range(row):
            for j in range(row):
                el = matrix[i][j]
                heapq.heappush(max_heap, -el)
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
                    
        return - max_heap[0]