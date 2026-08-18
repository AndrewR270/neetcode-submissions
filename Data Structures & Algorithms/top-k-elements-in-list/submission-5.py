class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = Counter(nums)
        heap = []
        for num, freq in occurrences.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]