class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for price in prices:
            startPrice = prices[l]
            if startPrice < price:
                res = max(res, price - startPrice)
            else:
                while price < startPrice: 
                    l += 1
                    startPrice = prices[l]
        
        return res