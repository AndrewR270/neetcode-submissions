class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = defaultdict(int)
        tChars = defaultdict(int)

        if len(s) == len(t):
            for char in s: sChars[char] += 1
            for char in t: tChars[char] += 1
            return sChars == tChars
        return False