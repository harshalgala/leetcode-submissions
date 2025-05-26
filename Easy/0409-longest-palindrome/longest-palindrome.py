class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)
        lonPal = 0
        for char in s:
            counter[char] += 1
            if counter[char] % 2 == 0:
                lonPal += 2
        for cnt in counter.values():
            if cnt % 2 == 1:
                lonPal += 1
                break
        return lonPal