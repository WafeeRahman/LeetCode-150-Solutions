class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        #Use a max heap to keep the closest points to origin at the end of the heap
        for x, y in points:
            dist = math.sqrt((x - 0)**2 + (y-0)**2)
            heapq.heappush(maxHeap, [-abs(dist),x, y])

        #Maintain a window of k length
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        res = []
        #When k nodes are left, iterate through each point and add coordinate tuple to result
        for i in range(len(maxHeap)):
            kTuple = [0, 0]
            kTuple[0] = maxHeap[i][1]
            kTuple[1] = maxHeap[i][2]
            res.append(kTuple)

        return res
        
        
        
