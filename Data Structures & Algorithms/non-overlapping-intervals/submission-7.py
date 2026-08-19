class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda x: x[0])
        cleaned = [intervals[0]]

        for start, end in intervals[1:]:
            if start < cleaned[-1][1]:
                cleaned[-1][1] = min(cleaned[-1][1], end)
                res += 1
            else: cleaned.append([start, end])
        return res
