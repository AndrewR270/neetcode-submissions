class Solution:
    def climbStairs(self, n: int) -> int:
        bestLast = 1
        bestBefore = 1

        for i in range(n-1):
            bestLast += bestBefore
            bestBefore = bestLast - bestBefore
        
        return bestLast