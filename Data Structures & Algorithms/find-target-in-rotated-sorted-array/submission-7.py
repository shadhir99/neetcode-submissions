class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for index, num in enumerate(nums):
        #     if num == target:
        #         return index
        # return -1

        # Always Compare nums[mid] and nums[r] since if nums[l] then you will miss min number

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        print(nums)
        print(pivot, nums[pivot])

        # Always compare nums[mid] and target and only update left , right pointers

        def binary_search(left:int, right:int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target :
                    left =  mid + 1
                else:
                    right = mid - 1
            return -1
        
        result = binary_search(0, pivot - 1)

        if result != -1:
            return result
        
        return binary_search(pivot, len(nums) - 1)
        