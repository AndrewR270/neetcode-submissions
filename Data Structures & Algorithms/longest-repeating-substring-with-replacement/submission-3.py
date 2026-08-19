class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        mostCommon = 0
        counts = defaultdict(int)
        left = 0

        for right, char in enumerate(s):
            counts[char] += 1
            mostCommon = max(mostCommon, counts[char])
            while (right - left + 1) - mostCommon > k:
                counts[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
