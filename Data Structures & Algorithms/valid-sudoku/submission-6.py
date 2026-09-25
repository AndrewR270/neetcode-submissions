class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Membership can be tracked with sets for unique
        # Must track row, col, and 3x3 portions
        # O(n^2) space allowed

        # Go over unique rows
        for r in range(len(board)):
            seen = set()
            for c in range(len(board)):
                element = board[r][c]
                if element == ".": continue
                else:
                    if element in seen: return False
                    seen.add(element)

        # Go over unique cols
        for c in range(len(board)):
            seen = set()
            for r in range(len(board)):
                element = board[r][c]
                if element == ".": continue
                else:
                    if element in seen: return False
                    seen.add(element)

        # Go over 3x3
        for gridX in range(3):
            for gridY in range(3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        element = board[r + 3*gridX][c + 3*gridY]
                        if element == ".": continue
                        else:
                            if element in seen: return False
                            seen.add(element)

        return True