class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = defaultdict(int)
        for i, n in enumerate(nums):
            if (target - n) in pairs:
                return [pairs[target-n], i]
            else: pairs[n] = i