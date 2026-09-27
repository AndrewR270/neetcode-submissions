class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = 0
        counts = defaultdict(int)
        counts[0] = 1

        for n in nums:
            prefixSum += n
            need = prefixSum - k
            res += counts[need]
            counts[prefixSum] += 1
        
        return res