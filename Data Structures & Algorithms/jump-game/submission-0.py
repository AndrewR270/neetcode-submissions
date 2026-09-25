class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for place, jump in enumerate(nums):
            if place > reach: return False
            reach = max(reach, place + jump)
        
        return True