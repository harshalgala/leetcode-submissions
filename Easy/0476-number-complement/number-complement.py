class Solution(object):
    def findComplement(self, num):
        yo = 1
        while yo <= num:
            yo = yo << 1
        return (yo-1)^num