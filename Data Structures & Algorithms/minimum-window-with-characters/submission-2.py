class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return

        tCount = defaultdict(int)
        for c in t: tCount[c] += 1
        window = defaultdict(int)
        have, need = 0, len(tCount)
        res = [-1, -1]
        resLen = float("inf")

        left = 0
        for right, char in enumerate(s):
            window[char] += 1
            if char in tCount and window[char] == tCount[char]: have += 1
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                    have -= 1
                left += 1
            
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""



        