
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        
        # max_len = 0

        # for i in range(len(s)):
            
        #     max_freq = 0
        #     count = {}
        #     for j in range(i, len(s)):
        #         count[s[j]] = count.get(s[j], 0) + 1
        #         max_freq = max(max_freq, count[s[j]])

        #         window_length = j - i + 1
        #         replacements = window_length - max_freq

        #         if replacements <= k:
        #             max_len = max(max_len, window_length)
            
        # return max_len


        # max_len = 0
        # count = {}
        # max_freq = 0
        # left = 0

        # for right in range(len(s)):

        #     # Count Frequency of Window
        #     count[s[right]] = count.get(s[right], 0) + 1
        #     max_freq = max(max_freq, count[s[right]])

        #     while (right - left + 1) - max_freq > k:
        #         count[s[left]] -= 1
        #         left += 1
        
        #     max_len = max(max_len, right - left + 1)

        # return max_len


        max_len = 0
        max_freq = 0
        count = {}
        left = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            window_length = right - left + 1
            
            max_len = max(max_len, window_length)
        
        return max_len





        