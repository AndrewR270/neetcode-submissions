class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)

        maxLength = 0
        maxFrequency = 0

        left = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            maxFrequency = max(maxFrequency, counts[s[right]])

            while (right - left + 1) - maxFrequency > k:
                counts[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength
        