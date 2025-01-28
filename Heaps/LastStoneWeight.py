class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)
        #Use a maxHeap to order the values from largest stone to smallest
        #Continue until there is atleast one stone left in the heap
        while len(maxHeap) > 1:
            #Take the top 2 stones
            x = heapq.heappop(maxHeap)
            x = -x
            y = maxHeap[0]
            y = -y
            #If the top 2 stones are equal, erase the second stone
            if x == y:
                heapq.heappop(maxHeap)
            else:
                #OTWS add the absolute value of the difference to the maxheap
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, -abs(x-y))
        #If theres a final stone, return it, otws all stones were destroyed
        if maxHeap:
            return abs(maxHeap[0])
        else:
            return 0
