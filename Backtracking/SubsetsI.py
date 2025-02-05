class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, subset):
            if i >= len(nums):
                #Subset persists between calls, copy it
                res.append(subset[:])
                return
            
            #Explore Decision Tree Where We Add Current Value to Subset
            subset.append(nums[i])
            backtrack(i+1, subset)
            
            #Vs Decision Tree Where We Do Not
            subset.pop()
            backtrack(i+1, subset)
            return 
       
        backtrack(0, [])
        return res

            
        
