class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        start, end = 0, 0
        while start < len(s):
            while s[end] != "#": end += 1
            length = int(s[start:end])
            strs.append(s[end+1:end+length+1])
            start = end + length + 1
            end = start + 1
        return strs


