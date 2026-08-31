class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        seen = {}
        max_count = 0
        left = 0
        max_freq = 0

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1
            max_freq = max(max_freq, seen[s[right]])


            while (right - left + 1) - max_freq > k:
                seen[s[left]] -= 1
                left += 1

            window_length = right - left + 1
            
            max_count = max(max_count, window_length)
        
        return max_count

        