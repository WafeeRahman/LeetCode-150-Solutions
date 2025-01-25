class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #Sorting will make duplicates adjacent

        for i in range(len(nums)):
            #Make sure that each first value is unique
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            #Two Pointers for the Jth and Kth Value
            l = i+1
            r = len(nums)-1
            
            #Since we sorted the array, we can use a two pointer
            #Approach to find a triplet with the current ith value that
            #Sums to Zero
            #Make sure that L is never equal to R, because that would mean
            #L and R are duplicate values
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    #Ensure that the next values of l and r are unique
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while r > l and nums[r] == nums[r+1]:
                        r-=1
        return res




