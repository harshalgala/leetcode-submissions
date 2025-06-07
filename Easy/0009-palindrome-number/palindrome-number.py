class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        print("Reverse :", reverse)
        xbackup = x
        print("xbackup :", xbackup)

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            # Floor division rounds down.
            x //=10
        print("Updated Reverse :", reverse)
        if reverse == xbackup:
            return True
        else:
            return False