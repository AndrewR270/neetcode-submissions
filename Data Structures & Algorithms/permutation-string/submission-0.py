class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        k = len(s1)
        chars = Counter(s1)
        window = defaultdict(int)

        for r, char in enumerate(s2):
            if r < k:
                window[char] += 1
            else:
                window[char] += 1
                window[s2[r-k]] -= 1

                if window[s2[r-k]] == 0:
                    del window[s2[r-k]]

            if window == chars: return True
        

        return False
            

