class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        minus2 = nums[0]
        minus1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(minus1, minus2 + nums[i])
            minus2, minus1 = minus1, curr
        
        return minus1