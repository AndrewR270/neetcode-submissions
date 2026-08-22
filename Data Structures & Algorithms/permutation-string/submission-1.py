class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        k = len(s1)
        chars = Counter(s1)
        window = defaultdict(int)

        for r, char in enumerate(s2):
            window[char] += 1
            if (r >= k):
                l = r-k
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
            
            if window == chars: return True
        
        return False
