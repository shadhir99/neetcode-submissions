import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for c in s.lower():
            if c.isalnum():
                new_s += c

        return new_s == new_s[::-1]
        