class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums == []:
            return []
        
        # for index, num in enumerate(nums):
        #     res = target - num
        #     if res in nums and nums.index(res) != index:
        #         print("Matched")
        #         return sorted([index, nums.index(res)])
        

        # Direct Two pointer won't work since we need to return indexes

        # A = []
        # for i, num in enumerate(nums):
        #     A.append([num, i])

        # A.sort()

        # left , right = 0, len(A) - 1

        # while left < right:
        #     result = A[left][0] + A[right][0]
        #     if result == target:
        #         return sorted([A[left][1], A[right][1]])
        #     elif result < target:
        #         left += 1
        #     else:
        #         right -= 1

        nums_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict:
                return [nums_dict[diff], i]
            nums_dict[num] = i
            
        return []
        