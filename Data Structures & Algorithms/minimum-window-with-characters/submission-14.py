class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""

        res, resLen = [-1, -1], float("inf")
        window = defaultdict(int)
        need = Counter(t)
        have = 0

        left = 0

        for right, char in enumerate(s):
            window[char] += 1
            if char in need and window[char] == need[char]: have += 1
            while have == len(need):
                if (right + 1 - left) < resLen:
                    res = [left, right + 1]
                    resLen = right + 1 - left
                window[s[left]] -= 1
                if window[s[left]] < need[s[left]]: have -= 1
                left += 1
        
        l, r = res
        return s[l:r] if resLen != float("inf") else ""



