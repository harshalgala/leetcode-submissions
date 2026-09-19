class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        high = 0
        low = float('inf')
        for p in prices: # 1
            if p < low: # 1 < 7
                low = p # 1
            elif p - low > high: #
                high = p - low # 7
        return high