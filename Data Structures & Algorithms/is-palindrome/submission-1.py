import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # new_s = ''
        # for c in s.lower():
        #     if c.isalnum():
        #         new_s += c

        # return new_s == new_s[::-1]

        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True
            
        
        