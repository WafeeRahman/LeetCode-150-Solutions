class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for i in range(len(nums)):
            #O(1) Lookup in a Set Base Case
            if nums[i] in numSet:
                return True
            #Add nums as encountered
            numSet.add(nums[i])
        return False
        