#With a rotated sorted array, we need to find a value at O(logn) time
#A rotated sorted array is rotated 1..n times, where the amount of rotations rotate
#The final value to the beginning of the array

#To find a value in log n time, we must use binary search
#To identify whether we are getting closer to target or not, we need to find the left sorted partition of 
#The rotated array, comparing the ends of the partition to target to see if we need to search the left sorted partition
#Or the right unsorted partition
class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l = 0 
        r = len(nums)-1

        while l<=r:

            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            #If we are in the left sorted partition and l > target, or target < mid, that means
            #That target is not in the current partition, move right
            #If one of these conditions fail that means target is in the left, continue to search further left
            if nums[l] <= nums[mid]:
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid-1
            else:
                #If we are in the right unsorted portion, and the num at mid is greater than the target
                #Or target is greater than the num at r, that tells us we need to check left
                #Since the array is rotated, and the target is greater than the num at r, we need to check left for greater vals
                #If the num at mid is greater than target, that tells us that target is to the left of mid in the rotated sorted arr
                if nums[mid] > target or nums[r] < target:
                    r = mid-1
                else:
                    l = mid+1
        return -1
              

        
