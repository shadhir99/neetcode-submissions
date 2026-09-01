class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x : x[0])

        output = [intervals[0]]

        result = 0

        for start, end in intervals[1:]:
            lastend = output[-1][1]
            if start < lastend:
                lastend = min(end, lastend)
                output[-1][1] = lastend
                result += 1
            else:
                output.append([start, end])
        
        return result