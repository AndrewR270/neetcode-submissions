class Solution:
    def climbStairs(self, n: int) -> int:
        total = 1
        trail = 1
        for i in range(n-1):
            total += trail
            trail = total - trail
        
        return total
