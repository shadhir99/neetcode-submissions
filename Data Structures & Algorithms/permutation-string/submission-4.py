from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # len_s1 = len(s1)
        # len_s2 = len(s2)
        # counter_s1 = Counter(s1)
        
        # for i in range(0, len_s2):
        #     counter_s2 = Counter(s2[i:i+len_s1])
        #     #print(s1, "-->",s2[i:i+len_s1])
        #     if counter_s1 == counter_s2:
        #         return True
        
        # return False
        # s1 = sorted(s1)

        # for i in range(len(s2)):
        #     for j in range(i, len(s2)):
        #         substr = sorted(s2[i:j+1])
        #         if s1 == substr:
        #             return True

        # return False

        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == s2_count:
            return True
        
        for j in range(len(s2) - len(s1)):
            s2_count[ord(s2[j]) - ord('a')] -= 1
            s2_count[ord(s2[j+len(s1)]) - ord('a')] += 1

            if s1_count == s2_count:
                return True
        
        return False



