class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()

        for i, n in enumerate(nums):
            if window and window[0] == i-k: window.popleft()
            while window and nums[window[-1]] < n: window.pop()
            window.append(i)
            if (i >= k - 1): res.append(nums[window[0]])
        
        return res
