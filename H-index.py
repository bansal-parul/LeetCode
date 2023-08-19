class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stock_price = prices[0]
        for i in range(1, len(prices)):
            current_profit = prices[i] - stock_price 
            if current_profit > profit:
                profit = current_profit
            stock_price = min(prices[i], stock_price )
        return profit
