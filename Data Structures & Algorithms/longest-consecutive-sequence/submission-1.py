class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums.sort()

        count = 1
        max_count = 1

        for i in range(1, len(nums)):

            if nums[i-1] == nums[i]:
                continue
            
            if nums[i-1] + 1 == nums[i]:
                count += 1
            else:
                count = 1
            
            max_count = max(max_count, count)        
        
        return max_count
