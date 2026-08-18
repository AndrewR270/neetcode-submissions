class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if not (r in range(rows) and c in range(cols) and
                (r,c) not in visited and grid[r][c] == "1"):
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dx, dy in directions:
                    r, c = row + dx, col + dy
                    if (r in range(rows) and c in range(cols) and
                        (r, c) not in visited and grid[r][c] == "1"):
                        visited.add((r,c))
                        q.append((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands
