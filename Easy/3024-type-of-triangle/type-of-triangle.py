class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Ensure triangle is made.
        if ((nums[0]+nums[1]) > nums[2] and (nums[1]+nums[2]) > nums[0] and (nums[0]+nums[2]) > nums[1]):
            triangle = True
        else:
            triangle = False
        triangleType = ""
        # If so then say what type.
        if ((nums[0] == nums[1]) and (nums[1] == nums[2])):
            triangleType = "equilateral"
        elif ( (nums[0] == nums[1]) or (nums[1] == nums[2]) or (nums[0] == nums[2]) ):
            triangleType = "isosceles"
        else:
            triangleType = "scalene"

        if triangle:
            return triangleType
        else:
            return "none"        