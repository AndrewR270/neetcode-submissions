class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        answer = nums[0]

        for num in nums[1:]:
            tempMax = max(num, num * maxProd, num * minProd)
            tempMin = min(num, num * maxProd, num * minProd)
            maxProd, minProd = tempMax, tempMin
            answer = max(answer, maxProd)
        
        return answer