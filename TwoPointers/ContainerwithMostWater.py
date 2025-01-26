class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curArea = 0
        maxArea = float('-inf')

        #Capture the maximum area at each step between
        #Two Pointers
        l = 0 
        r = len(heights)-1

        while l < r:
            #The Area at each point is
            #The distance between the two pointers
            #Multiplied by the height threshold between them
            curArea = (r-l) * min(heights[l], heights[r])
            #Change maxarea each time an area in the current window is greater
            maxArea = max(curArea, maxArea)
            
            #Traverse Right PTR if its ever less than or equal to 
            #Height at left ptr to test the next area
            if heights[r] <= heights[l]:
                r-=1

            #Traverse left if its ever less than right
            if heights[l] < heights[r]:
                l+=1

        return maxArea
