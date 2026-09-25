class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = defaultdict(int)

        for i, n in enumerate(nums):
            complement = target - n
            if complement in pairs: return [pairs[complement], i]
            pairs[n] = i