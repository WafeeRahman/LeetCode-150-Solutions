class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Two PTRS
        l = 0
        r = len(numbers)-1

        while l<=r:
            #If the smallest number + the largest is still less than target,
            #We need to traverse the left to get a larger number
            if numbers[l] + numbers[r] < target:
                l+=1
            #If the sum is greater than target
            #We need to traverse the right and get a smaller number
            elif numbers[r] + numbers[l] > target:
                r-=1
            else:
                #1-index and return
                return [l+1, r+1]
        return [-1,-1]

        
