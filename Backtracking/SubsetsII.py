class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        #Same as subsets, but ensure every first value is unique to avoid duplicate
        #Decision trees
        def backtrack(i, curSub):
            if i == len(nums):
                res.append(curSub.copy())
                return
            
            #Choose to add num
            curSub.append(nums[i])
            backtrack(i+1, curSub)
            curSub.pop()

            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, curSub)
            return 
        backtrack(0,[])
        return res


        
