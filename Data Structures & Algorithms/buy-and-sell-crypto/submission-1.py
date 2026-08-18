class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        if not prices:
            return 0
        low = prices[0]
        for i in range(len(prices)):
            if prices[i] <= low:
                low = prices[i]
                for j in range(i, len(prices)):
                    out = max(out, prices[j]-prices[i])
        return out