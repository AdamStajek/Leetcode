class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0
        for right in range(1, len(prices)):
            minimum = min(minimum, prices[right - 1])
            max_profit = max(max_profit, prices[right] - minimum)
        return max_profit





