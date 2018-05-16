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
        if a_t > - maxheap[0]:
            heapq.heappush(minheap, a_t)
        else:
            heapq.heappush(maxheap, -a_t)
            
        if len(minheap) == len(maxheap):
            print float(minheap[0] - maxheap[0]) / 2.0
        elif len(minheap) == len(maxheap) + 1:
            print float(minheap[0])
        elif len(maxheap) == len(minheap) + 1:
            print float(-maxheap[0])
    
        elif len(minheap) == len(maxheap) + 2:
            el = heapq.heappop(minheap)
            heapq.heappush(maxheap, -el)
            print float(minheap[0] - maxheap[0]) / 2.0
        elif len(maxheap) == len(minheap) + 2:
            el = heapq.heappop(maxheap)
            heapq.heappush(minheap, -el)
            print float(minheap[0] - maxheap[0]) / 2.0
            