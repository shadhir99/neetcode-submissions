from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if nums is None or nums == []:
            return False
        
        # for i in range(len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         if nums[i] == nums[j]:
        #             return True


        nums_dict = Counter(nums)

        for key, value in nums_dict.items():
            if value > 1:
                return True
        
        return False

    