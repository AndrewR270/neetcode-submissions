class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums)-1):
            res[i+1] = res[i] * nums[i]
        after = 1
        for i in range(len(nums)-1, 0, -1):
            after *= nums[i]
            res[i-1] *= after
        return res


        