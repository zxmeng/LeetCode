import heapq

n = int(raw_input().strip())
minheap = []
maxheap = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    if not minheap and not maxheap:
        heapq.heappush(maxheap, -a_t)
        print float(a_t)
        
    elif maxheap:
        # Insert/push the other streaming values
        if a_t > -maxheap[0]:
            heapq.heappush(minheap,a_t)
        else:
            heapq.heappush(maxheap,-a_t)

        # Calculate the median
        if len(maxheap)==len(minheap):
            print float(-maxheap[0]+minheap[0])/2
        elif len(maxheap)==len(minheap)+1:
            print float(-maxheap[0])
        elif len(minheap)==len(maxheap)+1:
            print float(minheap[0])

        # If min-heap and max-heap grow unbalanced we rebalance them by
        # removing/popping one element from a heap and inserting/pushing
        # it into the other heap, then we calculate the median
        elif len(minheap)==len(maxheap)+2:
            heapq.heappush(maxheap,-heapq.heappop(minheap))
            print float(-maxheap[0]+minheap[0])/2
        elif len(maxheap)==len(minheap)+2:
            heapq.heappush(minheap,-heapq.heappop(maxheap))
            print float(-maxheap[0]+minheap[0])/2