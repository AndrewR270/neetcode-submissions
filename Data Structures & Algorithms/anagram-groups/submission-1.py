class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            sortStr = ''.join(sorted(str))
            if sortStr not in anagrams: anagrams[sortStr] = [str]
            else: anagrams[sortStr].append(str)
        return list(anagrams.values())