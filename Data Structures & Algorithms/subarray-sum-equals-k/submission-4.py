class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        seen = {0:1}
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            needed = curr_sum - k

            if needed in seen:
                count += seen[needed]
            
            seen[curr_sum] = seen.get(curr_sum, 0) + 1
        
        return count