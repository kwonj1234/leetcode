class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = None
        profit = 0

        for price in prices:
            if current_min is None or price < current_min:
                current_min = price
            elif price > current_min:
                profit += price - current_min
                current_min = price
        
        return profit