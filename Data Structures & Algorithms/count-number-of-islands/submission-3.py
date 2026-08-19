class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if not (r in range(rows) and c in range(cols)
                and (r, c) not in visited and grid[r][c] == "1"):
                return
            visited.add((r,c))
            for direction in directions:
                dr, dc = direction
                dfs(r+dr, c+dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    res += 1
        
        return res
