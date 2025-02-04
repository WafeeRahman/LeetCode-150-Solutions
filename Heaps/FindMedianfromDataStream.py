class MedianFinder:

    def __init__(self):
        #Two Heaps Approach
        #Constraints, length difference cannot exceed 1
        #For O(1) lookup of medians
        self.smallHeap = [] #Max Heap for small values
        self.largeHeap = [] #Min Heap for large values

    def addNum(self, num: int) -> None:
    
        if self.smallHeap and num > abs(self.smallHeap[0]):
            heapq.heappush(self.largeHeap, num)
        else:
            heapq.heappush(self.smallHeap, -num)
        
        #Maintain Ordering Property for two heaps approach
        #Ensure that the length difference of each heap never exceeds one
        #If it does, add the top of the longer heap into the other
        #This will allow us to lookup the median at O(1)

        while abs(len(self.smallHeap) - len(self.largeHeap)) > 1:
            #Based on which heap is longer, heappush the top of the other into its counterpart
            if len(self.smallHeap) > len(self.largeHeap):
                mini = heapq.heappop(self.smallHeap)
                heapq.heappush(self.largeHeap, -mini) #Negate Val as Maxheaps are negative in python
            elif len(self.largeHeap) > len(self.smallHeap):
                mini = heapq.heappop(self.largeHeap)
                heapq.heappush(self.smallHeap, -mini) 
        print(self.smallHeap, self.largeHeap)

        

    def findMedian(self) -> float:
        
        totalLen = len(self.smallHeap) + len(self.largeHeap)
        if totalLen % 2 == 0:
            #Remember To DeNegate Max Heap Values
            return ((-(self.smallHeap[0]) + self.largeHeap[0])/2)
        else:
            if len(self.smallHeap) > len(self.largeHeap):
                #Remember To DeNegate Max Heap Values
                return -self.smallHeap[0]
            else:
                return self.largeHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
