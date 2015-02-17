class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        length = len(prices)
        if length <= 1:
            return 0
            
        result = 0
        bestbuy = prices[0]
        for i in range(1, length):
            if prices[i] - bestbuy > result:
                result = prices[i] - bestbuy
            if prices[i] < bestbuy:
                bestbuy = prices[i]
        return result
