class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ##Heaps Solution - heapify nums into a minheap, pop until we have a heap of len k
        #Get kth largest element
        
        ## Quick Select - Optimal
        ## QuickSort but we select the kth element when it lands on ppvt, 
        ## since we know everything to the left of ppvt is less, and everything to the right is greater

        def quickSelect(l, r, k):
            if l == r:
                return nums[l]
            
            pivot = nums[r]
            ppvt = l
            
            #Create a secondary pivot that ensures all values to the left
            #Are to the left of the pivot value at the end of the list
            #When there is a value less than pivot increment ppvt, swap with current value
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[ppvt] = nums[ppvt], nums[i]
                    ppvt += 1
                    print(pivot, ppvt, nums)
            #Afterwards, swap the secondary pivot value with the pivot value, thats at the end
            #So that everything thats left of the ppvt value is less, and vice versa w/ right
            nums[ppvt], nums[r] = nums[r], nums[ppvt]

            
            #If the ppvt is at the kth index, that tells us that it is the kth largest value
            #OTWS explore the sublist where its located
            if ppvt > k:
                return quickSelect(l, ppvt-1, k)
            if ppvt < k:
                return quickSelect(ppvt+1, r, k)
            else:
                print(nums)
                return nums[ppvt]
        
        return quickSelect(0, len(nums)-1, len(nums)-k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap =  nums
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return maxHeap[len(minHeap)-k]
