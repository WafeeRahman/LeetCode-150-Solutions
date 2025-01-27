class KthLargest:

    #Use a heap to maintain the numbers sorted from smallest to largest
    def __init__(self, k: int, nums: List[int]):
        #Keep the window size and heap as class variables
        self.kth = k
        self.heap = nums
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        #Ensure that the length of the heap is of k size so that we can
        #Find the kth largest in O(1) time
        while len(self.heap) > self.kth:
            heapq.heappop(self.heap)
        
        return self.heap[len(self.heap)-self.kth]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
