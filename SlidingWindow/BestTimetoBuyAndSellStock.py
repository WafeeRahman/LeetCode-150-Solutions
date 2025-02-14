class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        curProfit = 0
        #Sliding Window, find the window where profit is the largest
        for r in range(len(prices)):
            #Profit = price to sell - price bought initially
            curProfit = prices[r] - prices[l]
            #If we ever have a negative profit, lets slide our profit window to r
            #As negative profits mean the current window is not effective
            if curProfit < 0:
                l = r
            maxProfit = max(curProfit, maxProfit)
        return maxProfit
            
