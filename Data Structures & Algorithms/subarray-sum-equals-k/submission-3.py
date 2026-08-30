class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        
        # for i in range(len(nums)):
        #     if nums[i] == k:
        #         count += 1
        #     j = i + 1
        #     subarray_sum = nums[i]
        #     while j < len(nums):
        #         subarray_sum += nums[j]
        #         if subarray_sum == k:
        #             count += 1
        #         j += 1
            
        # return count

        # res = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             res += 1
        # return res


        count = 0
        seen = { 0 : 1 }
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            needed = current_sum - k

            if needed in seen:
                count += seen[needed]
            
            seen[current_sum] = seen.get(current_sum, 0) + 1

        return count





        

        