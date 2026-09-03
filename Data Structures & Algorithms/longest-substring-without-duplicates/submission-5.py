class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        max_len = 1
        
        count = {}

        left = 0

        for right in range(len(s)):

            while s[right] in count:
                    
                del count[s[left]]

                left += 1
            
            count[s[right]] = count.get(s[right], 0) + 1
                
            curr_len = right - left + 1

            max_len = max(max_len, curr_len)
        
        return max_len






        