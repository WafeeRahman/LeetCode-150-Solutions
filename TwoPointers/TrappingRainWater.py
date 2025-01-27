class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxHeightRight = 0
        maxHeightLeft = 0
        area = 0
        #Two Pointers
        while l <= r:
            lft = height[l]
            rgt = height[r]
            #Take the maximum height encountered at the left and right
            maxHeightLeft = max(maxHeightLeft, lft)
            maxHeightRight = max(maxHeightRight, rgt)
            #Take the minimum threshold where water can be filled between them
            maxHeight = min(maxHeightLeft, maxHeightRight)
            #If we encounter a height thats less than this threshold, that means water
            #Can be filled between the maxright and maxleft
            areaFillable = (maxHeight - height[l]) if (maxHeight - height[l]) > 0 else 0 
            areaFillable += (maxHeight - height[r]) if (maxHeight - height[r]) > 0 else 0 
            area += areaFillable

            #Traverse left and right based on the greater value
            if height[l] >= height[r]:
                r-=1
            if height[l] < height[r]:
                l+=1
        return area



            

        
