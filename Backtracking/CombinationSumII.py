class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curComb = []

        #At each step we have the decision to not include the current number in the tree, and sum, or to invlude it
        def backtrack(i, curSum):
            nonlocal res, curComb
            if i >= len(candidates) or curSum >= target:
                if curSum == target:
                    res.append(curComb.copy())
                return
          
            #Include value (supports dupes)
            curComb.append(candidates[i])
            backtrack(i+1, curSum+candidates[i])
            
            #Ensure that the next value is not a duplicate to avoid duplicate combinations when excluding the first val
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            #Dont include value and try all other values
            curComb.pop()
            backtrack(i+1, curSum)
        
        backtrack(0,0)
        return res
