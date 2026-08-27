class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0

        # for i in range(len(heights)):
        #     prod = 1
        #     for j in range(i+1, len(heights)):
        #         width = j - i
        #         height = min(heights[i], heights[j])
        #         prod = width * height        
        #     result = max(result, prod)

        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            result = max(area, result)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return result
        