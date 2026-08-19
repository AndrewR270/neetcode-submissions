class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counts = defaultdict(int)
        highestFreq = 0    
        left = 0

        for right, char in enumerate(s):
            counts[char] += 1
            highestFreq = max(highestFreq, counts[char])
            while (right - left + 1) - highestFreq > k:
                counts[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res