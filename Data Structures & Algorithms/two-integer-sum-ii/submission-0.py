class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hashmap = {}

        for index, num in enumerate(numbers):

            diff = target - num

            if diff in hashmap:

                return [hashmap[diff] + 1, index + 1]
            
            hashmap[num] = index
        
        return []
        
        