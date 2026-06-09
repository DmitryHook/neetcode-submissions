class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = 1

        max_profit = 0

        while sell_day < len(prices):
            if prices[sell_day] - prices[buy_day] < 0:
                buy_day = sell_day
            else:
                max_profit = max(max_profit, prices[sell_day] - prices[buy_day])
            sell_day += 1

        return max_profit