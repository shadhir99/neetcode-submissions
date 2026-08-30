from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        arr = []

        for num, cnt in count.items():
            arr.append([cnt, num])
        
        arr.sort(key=lambda x : x[0], reverse=True)

        for i in range(k):
            if i < k:
                result.append(arr[i][1])
        
        return result



        