class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: x[0])
        res.append(intervals[0])

        for start, end in intervals[1:]:
            lastIndex = res[-1][1]
            if start <= lastIndex:
                res[-1][1] = max(lastIndex, end)
            else:
                res.append([start, end])
        return res
