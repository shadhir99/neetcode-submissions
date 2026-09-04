class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_len = 1

        if len(s) == 1:
            return s

        result = s[0]

        left, right = 0, 1

        while left < len(s):

            right = left

            while right < len(s):

                test_string = s[left:right+1]

                if test_string == test_string[::-1]:

                    if len(test_string) > max_len:

                        result = test_string

                        max_len = len(test_string)

                right += 1

            left += 1

        return result





                



        
        