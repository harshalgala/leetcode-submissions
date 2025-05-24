class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complete = {}
        for i,j in enumerate(nums):
            leftOver = target - nums[i]

            if leftOver in complete:
                return [i,complete[leftOver]]
            else:
                complete[j]=i