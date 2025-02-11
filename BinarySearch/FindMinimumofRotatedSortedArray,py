#We're given an array of length n that was originally sorted
#It has now been rotated 1..n times, where n rotations mean i values from the end of the array 
#Were moved to the start of the array
#With this, we need to find the minimum value in the array, in log n time

#Log n time already tells us we need to use binary search, but how do we figure out where the traverse?
#Since the array is no longer sorted left to right
#Since the array was sorted and rotated, that gives us the garruntee that there are partitions of the array
#that are sorted in ascending order, and the mininum is always going to be in the right sorted portion granted
#That the array was not rotated n times back into its original form
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        r = len(nums) -1

        while l <= r:
            #If we are ever in a sorted portion of the array, test the minimum
            #Will return us the minimum if the array was sorted n times
            if nums[l] <= nums[r]:
                res = min(nums[l], res)    
            
            mid = (l+r)//2
            #If we are in the left sorted portion
            if nums[l] <= nums[mid]:
                res = min(nums[l], res)
                #check the right
                l = mid+1
            #If we are not i the left sorted portion, we are in the right
            #OTWS the left portion is unsorted, and we continue to search left for the sorted partition of the array
            #Since the array is rotated, the left is most likely to be sorted if !nums[l] <= nums[r]
            else:
                #Test nums[mid] against res, as the current portion is unsorted, mid can be the minimum itself
                res = min(nums[mid], res)
                r = mid-1
        return res
