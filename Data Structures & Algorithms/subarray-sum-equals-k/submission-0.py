class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = 0
        counts = {0: 1}

        for num in nums:
            prefixSum += num
            need = prefixSum - k
            if need in counts: res += counts[need]
            counts[prefixSum] = counts.get(prefixSum, 0) + 1
        
        return res