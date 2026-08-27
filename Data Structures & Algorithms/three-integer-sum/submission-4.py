class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #result = set()
        result = []

        nums.sort()

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             res = nums[i] + nums[j] + nums[k] 
        #             if res == 0:
        #                 result.add(tuple([nums[i], nums[j], nums[k]]))
        
        # return [list(res) for res in result]

        for i, a in enumerate(nums):
            # If First Number greater than 0, Then no possibility of getting 0 since remaining all numbers in the window will be positive after sorting 
            if a > 0:
                break
            
            # Skip Duplicate Number Processing
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                elif threeSum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 
            
        return result






