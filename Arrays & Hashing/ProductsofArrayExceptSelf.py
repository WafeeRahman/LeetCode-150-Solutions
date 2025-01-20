class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Explanation of Prefix Sums: 
        #With prefix sums, we can compute
        #The sum of all elements to the right of the current element
        #But not include the element itself

        prefix = 1
        productArr = []
        
        #Create an array of prefix products that exclude the current number
        for num in nums:
            productArr.append(prefix) #Exclude current number
            prefix *= num #Add to prefix product
        #Prefix Product for each number * PostFix Product for each number
        #Equals product of array except self
        postfix = 1
        print(productArr)
        
        for i in range(len(nums)-1,-1,-1):
            #Exclude Current Numbert
            productArr[i] = productArr[i] * postfix
            postfix *= nums[i] #Add to postfix
        
        return productArr
