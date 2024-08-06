class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        value = 0
        for step in nums:
            value += step
            if(value == 0):
                count += 1
        return count