#Given a target, find all combinations of each number in the candidates list where the sum of the combination = target
#At each step, we have the option of adding the same number again, or moving onto the next number
#If we sort the candidates, we can start from the smallest number to the largest, allowing us to skip larger values that
#Are gaurunteed to not add to target in recursive calls
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i, curComb):
            #Base Case, if we go out of bounds, or the current combination sum is >= target
            #We cannot add any new candidate, so we return, or if we overshoot target
            #Add a new combination if the sum is equal to the target
            if i >= len(candidates) or sum(curComb) >= target:
                if sum(curComb) == target:
                    res.append(curComb[:])
                return
            
            #Exhaust the current value and backtrack when we reach the base case
            #So that we explore the next candidate
            curComb.append(candidates[i])
            backtrack(i, curComb)
            curComb.pop()
            #Since we sorted candidates at the start, we can shortcut out of exploring any further
            #Candidates, as anything greater will not add to target
            if sum(curComb) + candidates[i] > target:
                return
            #OTWS explore the next candidate
            backtrack(i+1, curComb)
        
        backtrack(0, [])
        return res



        
