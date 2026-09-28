class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def rob(arr):
            prev2 = 0
            prev1 = 0
            for num in arr: prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1
        
        return max(rob(nums[1:]), rob(nums[:-1]))