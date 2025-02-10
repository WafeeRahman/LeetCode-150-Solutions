#Given a list of piles, we need to find the minimum amount of hours it takes to turn each pile to zero
#Where we can eat k piles at a time, meaning that piles[i] // k (rate at which each banana is eaten)
#Is the amount of hours it takes to eat the bananas
#We can use binary search to find the optimal amount of bananas to eat that will return us the minimum amount of hours
#The number of hours is always greater than the length of piles, meaning that
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles) #We can eat 1..MAX(PILES) bananas
        minK = r #The maximum bananas to eat to gurantee all piles eaten in h hours is the number of bananas is the max pile

        while l <= r:
            #Utilize Binary Search to quickly search for the optimal amount of bananas within this range
            k = (l+r)//2
            curHours = 0
            
            #Take the amount of hours it takes to eat all piles of bananas
            
            for i in range((len(piles))):
                curHours += math.ceil(piles[i]/k)
            
            print(curHours)
            if curHours > h:
                l=k+1

            elif curHours <= h:
                r=k-1
                minK = min(minK, k)
        
        return minK
        
        
