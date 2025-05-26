class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if len(str(abs(nums[i])))%2 == 0:
                result = result + 1
        return result