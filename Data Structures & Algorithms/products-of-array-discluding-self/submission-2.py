class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # result = []

        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             prod = prod * nums[j]
            
        #     result.append(prod)

        prod, zero_count = 1, 0

        for num in nums:
            if num != 0:
                prod *= num
            else:
                zero_count += 1
        
        result = [0] * len(nums)

        if zero_count > 1:
            return [0] * len(nums)

        for i in range(len(nums)):
            if zero_count:
                if nums[i] == 0:
                    result[i] = prod
                # else:
                #     result[i] = 0
            else:
                result[i] = prod // nums[i]
        
        return result


        