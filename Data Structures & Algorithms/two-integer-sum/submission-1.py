class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique = {}
        for i in range (len(nums)):
            unique[nums[i]] = i
        for i in range (len(nums)):
            complement = target-nums[i]
            if complement in unique and unique[complement] != i: 
                return[i, unique[complement]]
        
        