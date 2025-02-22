#Given an array of nums and a window size of k, there is a fixed sized of k sliding window that slides from the left of the array
#To the Right,
#Return an array of the max of each window
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #Keep track of the maximum within each window of size k within nums
        #W/ Sliding Window Technique
        q = deque() #Enqueue the maximum value that we encounter in each window
        res = []
        l = 0
        for r in range(len(nums)):
            #If we find a new max, empty the queue, and append the index of the current max
            #Value of the window
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)


            #If we reach the end of the current window of length k, take the maximum, which should always be
            #q[0], as we empty the queue and enque the max each time we see it
            while (r-l)+1 >= k:
                #If the current max value is no longer apart of the window
                #Pop it
                if l > q[0]:
                    maxOfCurWindow = q.popleft()
                res.append(nums[q[0]])
                l+=1
              
        return res
            


        
        
        
            


            


        
