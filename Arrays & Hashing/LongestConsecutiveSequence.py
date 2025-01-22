class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Lookup Values from the list in a set
        numSet=set(nums)
        maxCount = 0
        for i in range(len(nums)):
            #If the number isnt a consecutive value, it may be the start of a sequence
            if not (nums[i] - 1 in numSet):
                count = 0
                #Count Consecutive numbers that exist in the set with a loop
                while nums[i] + count in numSet:
                    count+=1
                #Take the max
                maxCount = max(count, maxCount)
        return maxCount

        
        
