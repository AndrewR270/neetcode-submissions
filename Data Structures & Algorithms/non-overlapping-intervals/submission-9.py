class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda x: x[0])
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < lastEnd:
                lastEnd = min(lastEnd, end)
                res += 1
            else:
                lastEnd = end
        return res