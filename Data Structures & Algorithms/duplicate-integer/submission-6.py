class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if nums is None or nums == []:
            return False
        
        # for i in range(len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         if nums[i] == nums[j]:
        #             return True


        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                return True

        # from collections import Counter

        # nums_dict = Counter(nums)

        # for key, value in nums_dict.items():
        #     if value > 1:
        #         return True
        
        return False

    