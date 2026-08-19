class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = set()
        left = 0

        for right, char in enumerate(s):
            while char in window:
                window.remove(s[left])
                left += 1
            window.add(char)
            res = max(res, right - left + 1)
        return res