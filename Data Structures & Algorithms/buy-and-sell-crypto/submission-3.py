class Solution:
    """
    patterns i notice:
    you always buy at the cheapest first possible price
    you always sell at the most expensive last possible price
    
    edge case: buying at the min number being at the end of the array

    if i iterate through the array and assume that i'm looking for the selling price
    i would want to maximize sell and minimize buy so that profit = sell - buy is maximized
    """
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyInd = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buyInd]:
                buyInd = i
            else:
                maxProfit = max(maxProfit, prices[i]-prices[buyInd])
        return maxProfit
