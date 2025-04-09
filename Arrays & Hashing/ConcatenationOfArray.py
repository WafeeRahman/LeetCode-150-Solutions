class Solution:
    #Given an integer array nums of length n, create an array that is 2n length
    #Where the nums in the orignal array keep their original spots, aswell as their spots in the added array
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #We can use python's built in array concatenation, but thats boring. 
        #return nums + nums

        #O(n) Solution, we know that when we move beyond n, the elements should still have their relative order
        #We can do this by using the modolus operator, and taking each ith position remaindered by N, where N
        #Is the length of the original list
        res = []
        n = len(nums)
        for i in range(2*n):
            res.append(nums[i%n])

        return res
        
