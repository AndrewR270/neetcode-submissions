class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = {}
        buckets = [[] for i in range(len(nums)+1)]
        for num in nums:
            occurrences[num] = 1 + occurrences.get(num, 0)
        for n,c in occurrences.items():
            buckets[c].append(n)
        res = []
        for i in reversed(range(len(buckets))):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return list(res)

        