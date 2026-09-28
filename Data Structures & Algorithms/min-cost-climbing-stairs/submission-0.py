class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minus2 = 0
        minus1 = 0

        for i in range(2, len(cost) + 1):
            curr = min(minus1 + cost[i-1], minus2 + cost[i-2])
            minus2, minus1 = minus1, curr
        
        return minus1