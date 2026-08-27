class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums == []:
            return []
        
        for index, num in enumerate(nums):
            res = target - num
            if res in nums and nums.index(res) != index:
                print("Matched")
                return sorted([index, nums.index(res)])
        
        return []
        