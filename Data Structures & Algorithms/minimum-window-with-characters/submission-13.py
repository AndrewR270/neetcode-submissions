class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        resLen = float("inf")

        need = Counter(t)
        have = 0

        window = defaultdict(int)
        left = 0

        for right, char in enumerate(s):
            window[char] += 1
            if window[char] == need[char]: have += 1
            while have == len(need):
                if (right - left + 1) < resLen:
                    res = [left, right + 1]
                    resLen = (right - left + 1)
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]: have -= 1
                left += 1
        l, r = res
        return s[l:r] if resLen != float("inf") else ""