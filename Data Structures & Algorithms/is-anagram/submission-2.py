from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        # return sorted(s) == sorted(t)

        # s_counter, t_counter = Counter(s), Counter(t)
        # return s_counter == t_counter

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        return all(i == 0 for i in count)

        