class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for a in digits:
            s += str(a)
        x = str(int(s) + 1)
        l = [int(a) for a in x]
        return l
