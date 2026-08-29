class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])

        # l, r = 0, 1
        # max_profit = 0
        
        # while r < len(prices):
        #     if prices[r] > prices[l]:
        #         profit = prices[r] - prices[l]
        #         max_profit = max(profit, max_profit)
        #     else:
        #         l = r
        #     r += 1

        # max_profit = 0
        # min_price = prices[0]

        # for price in prices[1:]:
        #     max_profit = max(max_profit, price - min_price)
        #     min_price = min(price, min_price)

        # return max_profit

        max_profit = 0

        buy = 0

        for sell in range(1, len(prices)):

            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            else:
                buy = sell
        return max_profit


