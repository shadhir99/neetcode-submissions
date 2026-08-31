class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []

        target = 0

        for i in range(len(nums)):

            if nums[i] > 0:
                break
            
            if nums[i] == nums[i-1] and i > 0:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                elif threeSum == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return result
        
                    
            



        