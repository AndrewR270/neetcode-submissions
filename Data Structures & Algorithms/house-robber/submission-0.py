class Solution:
    def rob(self, nums: List[int]) -> int:
        bestLast = 0
        bestBefore = 0

        for num in nums:
            newBest = max(bestLast, bestBefore + num)
            bestBefore = bestLast
            bestLast = newBest
        
        return bestLast