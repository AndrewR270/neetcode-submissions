class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            # compute hours needed at speed mid
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            
            if hours <= h:
                right = mid  # mid works, try smaller
            else:
                left = mid + 1  # mid too slow
        
        return left
