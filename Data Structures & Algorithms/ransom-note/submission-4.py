from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        r_dict = Counter(ransomNote)
        m_dict = Counter(magazine)

        for i in r_dict:
            if r_dict[i] > m_dict[i]:
                return False
        
        return True

