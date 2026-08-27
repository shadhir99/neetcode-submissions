from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len_s1 = len(s1)
        len_s2 = len(s2)
        counter_s1 = Counter(s1)
        
        for i in range(0, len_s2):
            counter_s2 = Counter(s2[i:i+len_s1])
            #print(s1, "-->",s2[i:i+len_s1])
            if counter_s1 == counter_s2:
                return True
        
        return False