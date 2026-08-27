class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])



        # l , r = 0, len(prices) - 1

        # while l < r:
        #     profit = max(profit, prices[r] - prices[l])

        #     if prices[r] > prices[l]:
        #         l += 1
        #     else:
        #         r -= 1
        
        return profit